import pandas as pd
from PyQt6.QtWidgets import QInputDialog,QTableWidgetItem
from UiFile import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.df = pd.read_csv("SampleData_NaN.csv")

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.refresh_data(self.df)
        self.pushButton.clicked.connect(lambda: self.refresh_data(self.df))
        self.pushButton_2.clicked.connect(self.replace_empty_values)
        self.pushButton_3.clicked.connect(self.count_empty_values)
        self.pushButton_4.clicked.connect(self.delete_empty_rows)
        self.pushButton_5.clicked.connect(self.fill_with_input)

    def refresh_data(self, df):
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.tableWidget.setItem(row, col, item)

    def replace_empty_values(self):
        process = self.df.fillna(True)
        self.refresh_data(process)

    def count_empty_values(self):
        empty_count = self.df.isna().sum().sum()
        self.label.setText(str(empty_count))

    def delete_empty_rows(self):
        process = self.df.dropna()
        self.refresh_data(process)

    def fill_with_input(self):
        user_input, ok = QInputDialog.getInt(self.MainWindow, "Input Replacement Value", "Enter value to replace empty cells:")
        if ok and user_input:
            process = self.df.fillna(user_input)
            self.refresh_data(process)

    def show(self):
        self.MainWindow.show()




