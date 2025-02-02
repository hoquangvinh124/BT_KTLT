from Ex99 import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox
import sys

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.moveRightButton.clicked.connect(self.one_arrow_1)
        self.moveLeftButton.clicked.connect(self.one_arrow_2)
        self.moveAllRightButton.clicked.connect(self.two_arrow_1)
        self.moveAllLeftButton.clicked.connect(self.two_arrow_2)
        self.removeClassAButton.clicked.connect(self.remove_class_a)
        self.removeClassBButton.clicked.connect(self.remove_class_b)
        self.updateButton.clicked.connect(self.process_name)
        self.finishButton.clicked.connect(self.process_exit)

    def process_name(self):
        name = str(self.lineEdit.text())
        if name.strip() != '':
            self.listWidgetA.addItem(name)

    def one_arrow_1(self):
        current_name = self.listWidgetA.currentRow()
        self.listWidgetB.addItem(self.listWidgetA.takeItem(current_name))

    def two_arrow_1(self):
        while self.listWidgetA.count() > 0:
            item = self.listWidgetA.takeItem(0)
            self.listWidgetB.addItem(item)

    def one_arrow_2(self):
        current_name = self.listWidgetB.currentRow()
        self.listWidgetA.addItem(self.listWidgetB.takeItem(current_name))

    def two_arrow_2(self):
        while self.listWidgetB.count() > 0:
            item = self.listWidgetB.takeItem(0)
            self.listWidgetA.addItem(item)

    def remove_class_a(self):
        self.listWidgetA.clear()

    def remove_class_b(self):
        self.listWidgetB.clear()

    def process_exit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Confirmation Exit")
        dlg.setText("Are you sure you want to Exit?")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            sys.exit(0)

    def show(self):
        self.MainWindow.show()