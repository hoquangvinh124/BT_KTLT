from find_negative import Ui_MainWindow
import re

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.NegativeNumberInStrings)

    def NegativeNumberInStrings(self):
        s = self.lineEdit.text()
        negative_numbers = re.findall(r'-\d+', s)
        negative_numbers = list(map(str, negative_numbers))
        return self.lineEdit_2.setText(" ".join(negative_numbers))

    def show(self):
        self.MainWindow.show()
