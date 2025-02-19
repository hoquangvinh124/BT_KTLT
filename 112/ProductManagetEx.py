from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from ProductManagement import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.databasePath="databases/drinks.sqlite"
        self.selectedRecord=None
        self.selectedRow=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.connectDatabase()
        self.loadProduct()
        self.pushButtonNew.clicked.connect(self.processNew)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.processItemSelection)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.pushButtonRemove.clicked.connect(self.processRemove)

    def connectDatabase(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(self.databasePath)
        self.db.open()
        self.model = QSqlTableModel(db=self.db)

    def loadProduct(self):
        tableName = "beverages"
        self.model.setTable(tableName)
        self.model.select()
        self.tableWidgetProduct.setRowCount(0)
        for i in range(self.model.rowCount()):
            self.tableWidgetProduct.insertRow(i)
            record = self.model.record(i)
            itemId = QTableWidgetItem(str(record.value(0)))
            itemProductCode = QTableWidgetItem(str(record.value(1)))
            itemProductName = QTableWidgetItem(str(record.value(2)))
            itemUnitPrice = QTableWidgetItem(str(record.value(3)))
            self.tableWidgetProduct.setItem(i, 0, itemId)
            self.tableWidgetProduct.setItem(i, 1, itemProductCode)
            self.tableWidgetProduct.setItem(i, 2, itemProductName)
            self.tableWidgetProduct.setItem(i, 3, itemUnitPrice)

    def processNew(self):
        self.lineEditProductId.setText("")
        self.lineEditProductName.setText("")
        self.lineEditUnitPrice.setText("")
        self.lineEditProductId.setFocus()
        self.selectedRecord=None
        self.selectedRow=None

    def processItemSelection(self):
        self.selectedRow=self.tableWidgetProduct.currentRow()
        if self.selectedRow==-1:
            return
        self.selectedRecord=self.model.record(self.selectedRow)
        productCode=self.selectedRecord.value(1)
        productName=self.selectedRecord.value(2)
        unitPrice=self.selectedRecord.value(3)
        self.lineEditProductId.setText(productCode)
        self.lineEditProductName.setText(productName)
        self.lineEditUnitPrice.setText(str(unitPrice))

    def processSave(self):
        if self.selectedRecord is None:
            record = self.model.record()
            record.setValue(1, self.lineEditProductId.text())
            record.setValue(2, self.lineEditProductName.text())
            record.setValue(3, float(self.lineEditUnitPrice.text()))
            if self.model.insertRecord(-1, record):
                if self.model.submitAll():
                    self.loadProduct()
                    self.selectedRecord = record
                    self.selectedRow = self.model.rowCount() - 1
        else:
            self.selectedRecord.setValue(1, self.lineEditProductId.text())
            self.selectedRecord.setValue(2, self.lineEditProductName.text())
            self.selectedRecord.setValue(3, float(self.lineEditUnitPrice.text()))
            self.model.setRecord(self.selectedRow, self.selectedRecord)
            if self.model.submitAll():
                self.loadProduct()

    def processRemove(self):
        dlg = QMessageBox(self.MainWindow)
        if self.selectedRecord == None:
            dlg.setWindowTitle("Deleteing error")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setText("You have to select a Product to delete")
            dlg.exec()
            return
        dlg.setWindowTitle("Confirmation Deleting")
        dlg.setText("Are you sure you want to delete?")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            result=self.model.removeRow(self.selectedRow)
            if result == True:
                self.loadProduct()
                self.processNew()

    def show(self):
        self.MainWindow.show()