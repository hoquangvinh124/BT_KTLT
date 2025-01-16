from ka_ku_la_to import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def show(self):
        self.MainWindow.show()