from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem
from ExcelHandle import *
from soft import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.EmployeeList = ExcelHandle.read_employees_from_excel("employees.xlsx")

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.load_data()
        self.tableWidget.cellClicked.connect(self.display_employee_details)
        self.pushButton_2.clicked.connect(self.sort_employees_by_age)

    def load_data(self):
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(self.EmployeeList))
        self.tableWidget.setHorizontalHeaderLabels(["STT", "Mã", "Tên", "Tuổi"])
        for row_idx, employee in enumerate(self.EmployeeList):
            item_stt = QTableWidgetItem(str(employee.stt))
            item_stt.setData(Qt.ItemDataRole.UserRole, employee)
            self.tableWidget.setItem(row_idx, 0, item_stt)
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(employee.code)))
            self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(employee.name)))
            self.tableWidget.setItem(row_idx, 3, QTableWidgetItem(str(employee.age)))

    def display_employee_details(self, row, column):
        item = self.tableWidget.item(row, 0)
        employee = item.data(Qt.ItemDataRole.UserRole)
        self.lineEdit_ID.setText(str(employee.stt))
        self.lineEdit_FullName.setText(str(employee.code))
        self.lineEdit_Address.setText(employee.name)
        self.lineEdit_Birth.setText(str(employee.age))

    def sort_employees_by_age(self):
        self.EmployeeList = sorted(self.EmployeeList, key=lambda e: e.age)
        self.load_data()

    def show(self):
        self.MainWindow.show()
