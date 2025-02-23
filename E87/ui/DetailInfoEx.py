from PyQt6.QtWidgets import QDialog
from E87.ui.DetailInfo import Ui_Dialog
from E87.ui.MainPageEx import MainWindowEx
from E87.class_info import *
from E87.lib.CSVFactory import CSVFileFactory

class DetailInfoDialog(QDialog, Ui_Dialog, MainWindowEx):
    def __init__(self, customer):
        MainWindowEx.__init__(self)
        self.setupUi(self)
        self.listcustomer = self.ListCustomer
        self.lineEditID.setText(customer.name)
        self.lineEditName.setText(customer.code)
        self.lineEditPhone.setText(customer.phone)
        self.lineEditEmail.setText(customer.email)
        self.pushButton.clicked.connect(self.update_button)
        self.pushButton_2.clicked.connect(self.remove_button)

    def update_button(self):
        name = str(self.lineEditID.text())
        code = str(self.lineEditName.text())
        phone = str(self.lineEditPhone.text())
        email = str(self.lineEditEmail.text())
        obj = Customer(code, name, phone, email)
        for i, c in enumerate(self.listcustomer):
            if c.code == obj.code:
                self.ListCustomer[i] = obj
        CSVFileFactory.write_data(self.listcustomer, "../data/customer.csv")
        self.accept()

    def remove_button(self):
        code = str(self.lineEditName.text())
        for i, c in enumerate(self.listcustomer):
            if c.code == code:
                self.ListCustomer.pop(i)
        CSVFileFactory.write_data(self.listcustomer, "../data/customer.csv")
        self.accept()

