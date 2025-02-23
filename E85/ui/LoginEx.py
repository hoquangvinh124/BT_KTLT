from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6.QtCore import pyqtSignal, QObject
from E85.Lib.DataConnector import DataProcessing
from E85.ui.Login import Ui_MainWindow
from E85.ui.MainPageEx import MainWindowEx

class LoginMainWindowEx(Ui_MainWindow, QObject):
    login_successful = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        QObject.__init__(self)
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonLogin.clicked.connect(self.process_login)

    def process_login(self):
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        emp = DataProcessing.login_auth(username, password)
        if emp is not None:
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = MainWindowEx()
            self.myui.setupUi(self.mainwindow)
            self.login_successful.connect(self.myui.handle_login)
            self.myui.handle_login(emp)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()

    def show(self):
        self.MainWindow.show()
