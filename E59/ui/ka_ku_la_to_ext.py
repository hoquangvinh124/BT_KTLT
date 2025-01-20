from ka_ku_la_to import Ui_MainWindow
from E59.lib.code import Fraction

class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.subtract)
        self.pushButton_3.clicked.connect(self.multiply)
        self.pushButton_4.clicked.connect(self.divide)

    def add(self):
        tu1 = int(self.lineEdit.text())
        mau1 = int(self.lineEdit_2.text())
        tu2 = int(self.lineEdit_3.text())
        mau2 = int(self.lineEdit_4.text())
        f1 = Fraction(tu1, mau1)
        f2 = Fraction(tu2, mau2)
        result = Fraction.add(f1, f2)
        self.label_10.setText("+")
        return (self.label_9.setText(f'{result.numerator}'),
                self.label_7.setText(f'{result.denominator}'))

    def subtract(self):
        tu1 = int(self.lineEdit.text())
        mau1 = int(self.lineEdit_2.text())
        tu2 = int(self.lineEdit_3.text())
        mau2 = int(self.lineEdit_4.text())
        f1 = Fraction(tu1, mau1)
        f2 = Fraction(tu2, mau2)
        result = Fraction.subtract(f1, f2)
        self.label_9.setText(f'{result.numerator}')
        self.label_7.setText(f'{result.denominator}')
        self.label_10.setText("-")

    def multiply(self):
        tu1 = int(self.lineEdit.text())
        mau1 = int(self.lineEdit_2.text())
        tu2 = int(self.lineEdit_3.text())
        mau2 = int(self.lineEdit_4.text())
        f1 = Fraction(tu1, mau1)
        f2 = Fraction(tu2, mau2)
        result = Fraction.multiply(f1, f2)
        self.label_9.setText(f'{result.numerator}')
        self.label_7.setText(f'{result.denominator}')
        self.label_10.setText("*")

    def divide(self):
        tu1 = int(self.lineEdit.text())
        mau1 = int(self.lineEdit_2.text())
        tu2 = int(self.lineEdit_3.text())
        mau2 = int(self.lineEdit_4.text())
        f1 = Fraction(tu1, mau1)
        f2 = Fraction(tu2, mau2)
        self.label_10.setText("/")
        try:
            result = Fraction.divide(f1, f2)
            self.label_9.setText(f'{result.numerator}')
            self.label_7.setText(f'{result.denominator}')
        except ZeroDivisionError:
            pass

    def show(self):
        self.MainWindow.show()