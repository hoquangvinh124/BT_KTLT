from Palindrome import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.execute)

    def check_palindrome(self, s):
        if len(s) <= 1:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def execute(self):
        s = str(self.lineEdit.text())
        s = s.lower()
        if self.check_palindrome(s):
            self.label_4.setText("YES")
            self.label_4.setStyleSheet("font-size: 12pt; font-weight: bold; color: green; padding-left: 25px;")
        else:
            self.label_4.setText("NO")
            self.label_4.setStyleSheet("font-size: 12pt; font-weight: bold; color: red; padding-left: 25px;")

    def show(self):
        self.MainWindow.show()
