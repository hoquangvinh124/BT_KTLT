from Trinh_Tran_Phuong_Tuan import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.standardized)
        
    def standardized(self):
        return self.lineEdit.setText(" ".join(self.lineEdit.text().split()).title())

    def show(self):
        self.MainWindow.show()
