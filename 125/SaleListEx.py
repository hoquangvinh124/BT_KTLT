import pandas as pd
from PyQt6.QtWidgets import QTableWidgetItem

from SaleList import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.display_list_employee()


    def display_list_employee(self):
        df = pd.read_excel("Sales.xlsx")
        self.tableWidget.setRowCount(len(df))
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(["Week", "Sales_Volume", "Price", "Ads_Cost"])
        for i in range(len(df)):
            Week = QTableWidgetItem(str(df["Week"].iloc[i]))
            Sales_Volume = QTableWidgetItem(str(df["Sales_Volume"].iloc[i]))
            Price = QTableWidgetItem(str(df["Price"].iloc[i]))
            Ads_Cost = QTableWidgetItem(str(df["Ads_Cost"].iloc[i]))
            self.tableWidget.setItem(i, 0, Week)
            self.tableWidget.setItem(i, 1, Sales_Volume)
            self.tableWidget.setItem(i, 2, Price)
            self.tableWidget.setItem(i, 3, Ads_Cost)

    def show(self):
        self.MainWindow.show()
