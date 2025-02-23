import pandas as pd
from PyQt6.QtWidgets import QTableWidgetItem

from employeelist import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.display_list_employee()

    def display_list_employee(self):
        df = pd.read_csv("employee.csv")
        self.tableWidget.setRowCount(len(df))
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(["Id", "Name", "Dob", "Role"])
        for i in range(len(df)):
            employee_id = QTableWidgetItem(str(df["Id"].iloc[i]))
            name = QTableWidgetItem(str(df["Name"].iloc[i]))
            dob = QTableWidgetItem(str(df["Dob"].iloc[i]))
            role = QTableWidgetItem(str(df["Role"].iloc[i]))
            self.tableWidget.setItem(i, 0, employee_id)
            self.tableWidget.setItem(i, 1, name)
            self.tableWidget.setItem(i, 2, dob)
            self.tableWidget.setItem(i, 3, role)

    def show(self):
        self.MainWindow.show()
