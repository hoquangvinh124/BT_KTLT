from E71.ui.BlueLock_Bank import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMessageBox, QDialog, QLabel, QInputDialog
from E71.class_info.class_info import *

class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.Baking_system = Bank()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.add_booking)
        self.pushButton_2.clicked.connect(self.remove_by_id)
        self.create_button(self.Baking_system.account_info())
        self.pushButton_4.clicked.connect(self.transfer_money)
        self.pushButton_3.clicked.connect(self.withdraw_money)
        self.pushButton_6.clicked.connect(self.show_balance)
        self.pushButton_7.clicked.connect(self.deposit_money)
        self.pushButton_5.clicked.connect(self.show_transaction_history)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def create_button(self, list):
        self.clear_layout(self.verticalLayoutButton)
        for acc in list:
            btn = QPushButton(acc.get_info())
            btn.clicked.connect(lambda _, a=acc: self.show_accounts_details(a))
            self.verticalLayoutButton.addWidget(btn)

    def show_accounts_details(self, a):
        self.lineEdit.setText(f"{a.account_number}")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText(f"{a.name}")

    def add_booking(self):
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        name = str(self.lineEdit_3.text())
        exist = False
        if account_number in self.Baking_system.accounts.keys():
            exist = True
            print("Da co tai khoan voi ID nay ton tai")
        if not exist and account_number != '' and pin != '' and name != '':
            self.Baking_system.add_account(Account(account_number, pin, name))
        self.create_button(self.Baking_system.account_info())

    def remove_by_id(self):
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        success = False
        if self.Baking_system.authenticate(account_number, pin):
            self.Baking_system.cancel_account(account_number)
        if not success:
            print("Sai ma Pin/Khong tim thay account de dong ")
        self.create_button(self.Baking_system.account_info())

    def show_transaction_history(self):
        account = None
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        if account_number in self.Baking_system.accounts.keys():
            if self.Baking_system.authenticate(account_number, pin):
                account = self.Baking_system.accounts[account_number]
        try:
            dialog = QDialog()
            dialog.setWindowTitle("Transaction History")
            layout = QVBoxLayout()
            history = "\n".join(account.get_transaction_history())
            label = QLabel(f"Transaction History:\n{history}")
            layout.addWidget(label)
            dialog.setLayout(layout)
            dialog.exec()
        except Exception:
            print("Incorrect PIN")

    def show_balance(self):
        account = None
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        if account_number in self.Baking_system.accounts.keys():
            if self.Baking_system.authenticate(account_number, pin):
                account = self.Baking_system.accounts[account_number]
        try:
            dialog = QDialog()
            dialog.setWindowTitle("Account Balance")
            layout = QVBoxLayout()
            balance_info = account.get_balance()
            label = QLabel(balance_info)
            layout.addWidget(label)
            dialog.setLayout(layout)
            dialog.exec()
        except Exception:
            print("Incorrect PIN")

    def withdraw_money(self):
        account = None
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        if account_number in self.Baking_system.accounts.keys():
            if self.Baking_system.authenticate(account_number, pin):
                account = self.Baking_system.accounts[account_number]
        try:
            amount, ok = QInputDialog.getInt(None, "Withdraw Money", "Enter amount to withdraw:")
            if ok:
                result = account.withdraw(amount)
                QMessageBox.information(None, "Withdraw Result", result)
        except Exception:
            print("Incorrect PIN")

    def transfer_money(self):
        account = None
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        if account_number in self.Baking_system.accounts.keys():
            if self.Baking_system.authenticate(account_number, pin):
                account = self.Baking_system.accounts[account_number]
        receiver_account_number, ok = QInputDialog.getText(None, "Transfer Money", "Enter recipient account number:")
        if ok and receiver_account_number in self.Baking_system.accounts.keys():
            receiver = self.Baking_system.accounts[receiver_account_number]
            amount, ok = QInputDialog.getInt(None, "Transfer Money", "Enter amount to transfer:")
            if ok:
                result = account.transfer(receiver, amount)
                QMessageBox.information(None, "Transfer Result", result)
        else:
            QMessageBox.warning(None, "Error", "Invalid recipient account number.")

    def deposit_money(self):
        account = None
        account_number = str(self.lineEdit.text())
        pin = str(self.lineEdit_2.text())
        if account_number in self.Baking_system.accounts.keys():
            if self.Baking_system.authenticate(account_number, pin):
                account = self.Baking_system.accounts[account_number]
        try:
            amount, ok = QInputDialog.getInt(None, "Deposit Money", "Enter amount to deposit:")
            if ok:
                result = account.deposit(amount)
                QMessageBox.information(None, "Deposit Result", result)
        except Exception:
            print("Incorrect PIN")

    def show(self):
        self.MainWindow.show()


