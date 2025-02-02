from soft import Ui_MainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QInputDialog, QMessageBox

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.listWidget.addItem("Meta Verse")
        self.listWidget.item(0).setIcon(QIcon(r"../images/ic_metaverse.png"))
        self.listWidget.addItem("Smart Contract")
        self.listWidget.item(1).setIcon(QIcon(r"../images/ic_smartcontract.png"))
        self.listWidget.addItems(["Learn Python", "Machine Learning", "Deep Learning"])

        self.btnAddNew.clicked.connect(self.addItem)
        self.btnInsert.clicked.connect(self.insertItem)
        self.btnClear.clicked.connect(self.clearAll)
        self.btnRemove.clicked.connect(self.removeItem)
        self.btnUpdate.clicked.connect(self.updateItem)
        self.listWidget.itemClicked.connect(self.processItemClicked)
        self.listWidget.itemDoubleClicked.connect(self.processItemDoubleClicked)
        self.listWidget.itemSelectionChanged.connect(self.processItemSelectionChanged)

    def processItemSelectionChanged(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        self.MainWindow.setWindowTitle(item.text())

    def processItemDoubleClicked(self):
        self.updateItem()

    def processItemClicked(self):
        current_row = self.listWidget.currentRow()
        data = self.listWidget.item(current_row)
        print("itemClicked=", data.text())

    def addItem(self):
        text, ok = QInputDialog.getText(self.MainWindow, 'Add a New Data', 'New Data:')
        if ok and text:
            self.listWidget.addItem(text)

    def updateItem(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            item = self.listWidget.item(current_row)
            text, ok = QInputDialog.getText(self.MainWindow, 'Update Data', 'New Data:', text=item.text())
            if ok and text:
                item.setText(text)

    def insertItem(self):
        text, ok = QInputDialog.getText(self.MainWindow, 'Insert a New Data', 'New Data:')
        if ok and text:
            current_row = self.listWidget.currentRow()
            self.listWidget.insertItem(current_row + 1, text)

    def removeItem(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            item = self.listWidget.item(current_row)
            msg = QMessageBox()
            msg.setText(f"Are you sure you want to remove {item.text()}?")
            msg.setWindowTitle("Removing Confirmation")
            msg.setIcon(QMessageBox.Icon.Question)
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            msg.setStandardButtons(buttons)
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                current_item = self.listWidget.takeItem(current_row)
                del current_item

    def clearAll(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to clear all Data?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.listWidget.clear()

    def show(self):
        self.MainWindow.show()
