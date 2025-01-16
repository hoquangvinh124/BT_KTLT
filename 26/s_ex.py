from s import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.btn1.clicked.connect(self.count_uppercase)
        self.btn2.clicked.connect(self.count_lowercase)
        self.btn3.clicked.connect(self.count_numbers)
        self.btn4.clicked.connect(self.count_special_characters)
        self.btn5.clicked.connect(self.count_spaces)
        self.btn6.clicked.connect(self.count_vowels)
        self.btn7.clicked.connect(self.count_consonants)

    def count_uppercase(self):
        sum = 0
        for c in str(self.plainTextEdit.toPlainText()):
            if c.isupper():
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def count_lowercase(self):
        sum = 0
        for c in str(self.plainTextEdit.toPlainText()):
            if c.islower():
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def count_numbers(self):
        sum = 0
        for c in str(self.plainTextEdit.toPlainText()):
            if c.isdigit():
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def count_special_characters(self):
        sum = 0
        for c in str(self.plainTextEdit.toPlainText()):
            if not c.isalnum() and not c.isspace():
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def count_spaces(self):
        sum = 0
        for c in str(self.plainTextEdit.toPlainText()):
            if c.isspace():
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def count_vowels(self):
        sum = 0
        vowels = "aeiouAEIOU"
        for c in str(self.plainTextEdit.toPlainText()):
            if c in vowels:
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def count_consonants(self):
        sum = 0
        vowels = "aeiouAEIOU"
        for c in str(self.plainTextEdit.toPlainText()):
            if c.isalpha() and c not in vowels:
                sum += 1
        return self.plainTextEdit_2.setPlainText(str(sum))

    def show(self):
        self.MainWindow.show()
