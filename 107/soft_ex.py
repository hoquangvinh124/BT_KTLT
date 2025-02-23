from PyQt6.QtWidgets import QTableWidgetItem

from ExcelHandle import *
from soft import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.StudentList = ExcelManager("students.xlsx").read_excel()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.load_data()
        self.tableWidget.cellClicked.connect(self.display_student_details)


    def load_data(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(self.StudentList))
        self.tableWidget.setHorizontalHeaderLabels(
            ["Mã SV", "Họ và Tên", "Địa Chỉ", "Ngày Sinh", "SĐT"]
        )
        for row_idx, student in enumerate(self.StudentList):
            self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(student.student_id))
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(student.full_name))
            self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(student.address))
            self.tableWidget.setItem(row_idx, 3, QTableWidgetItem(student.date_of_birth))
            self.tableWidget.setItem(row_idx, 4, QTableWidgetItem(student.phone_number))

    def display_student_details(self, row, column):
        student = self.StudentList[row]
        self.lineEdit_ID.setText(student.student_id)
        self.lineEdit_FullName.setText(student.full_name)
        self.lineEdit_Address.setText(student.address)
        self.lineEdit_Birth.setText(student.date_of_birth)
        self.lineEdit_Phone.setText(student.phone_number)

    def show(self):
        self.MainWindow.show()


