from PyQt6.QtWidgets import QApplication, QMainWindow

from find_negative_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()