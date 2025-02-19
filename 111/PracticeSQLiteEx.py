import os.path

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PracticeSQLite import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.processPickSQLite)
        self.comboBox.activated.connect(self.processSelectedTable)
        self.pushButton_2.clicked.connect(self.processFetchMore)

    def processPickSQLite(self):
        filters = "SQLite database (*.sqlite);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.MainWindow,
            filter=filters,
        )
        self.lineEdit.setText(filename)
        baseDir = os.path.dirname(__file__)
        databasePath = os.path.join(baseDir, filename)
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(databasePath)
        self.db.open()
        tables = self.db.tables()
        self.comboBox.clear()
        for i in range(len(tables)):
            tableName = tables[i]
            self.comboBox.addItem(tableName)

    def processSelectedTable(self):
        tableName = self.comboBox.currentText()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable(tableName)
        self.model.select()
        self.tableWidget.setRowCount(0)
        self.columns = self.model.record().count()
        self.tableWidget.setColumnCount(self.columns)
        labels = []
        for i in range(self.columns):
            fieldName = self.model.record().fieldName(i)
            labels.append(fieldName)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        for i in range(self.model.rowCount()):
            self.tableWidget.insertRow(i)
            record = self.model.record(i)
            for j in range(self.columns):
                item = QTableWidgetItem(str(record.value(j)))
                self.tableWidget.setItem(i, j, item)

    def processFetchMore(self):
        if self.model.canFetchMore():
            i = self.model.rowCount()
            self.model.fetchMore()
            for i in range(i, self.model.rowCount()):
                self.tableWidget.insertRow(i)
                record = self.model.record(i)
                for j in range(self.columns):
                    item = QTableWidgetItem(str(record.value(j)))
                    self.tableWidget.setItem(i, j, item)
        else:
            msg = QMessageBox()
            msg.setText("No more records to fetch")
            msg.exec()

    def show(self):
        self.MainWindow.show()