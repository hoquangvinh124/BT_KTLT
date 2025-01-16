from math import factorial

from calculation import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.permutation)
        self.pushButton.clicked.connect(self.combination)

    def factorial(self, n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    def permutation(self):
        N = int(self.lineEdit.text())
        K = int(self.lineEdit_2.text())
        fac_of_N = factorial(N)
        fac_of_N_K = factorial(N - K)
        res = fac_of_N / fac_of_N_K
        return self.lineEdit_3.setText(f"{res:.0f}")

    def combination(self):
        N = int(self.lineEdit.text())
        K = int(self.lineEdit_2.text())
        fac_of_N = factorial(N)
        fac_of_N_K = factorial(N - K)
        fac_of_K = factorial(K)
        res = fac_of_N / (fac_of_N_K * fac_of_K)
        return self.lineEdit_4.setText(f"{res:.0f}")

    def show(self):
        self.MainWindow.show()
