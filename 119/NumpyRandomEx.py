from NumpyRandom import Ui_MainWindow
import numpy as np

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
       pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.generate_matrix)

    def generate_matrix(self):
        row = self.lineEdit.text()
        column = self.lineEdit_2.text()
        matrix = np.random.randint(0, 10, (int(row), int(column)))
        self.label_4.setText(str(matrix))

    def show(self):
        self.MainWindow.show()