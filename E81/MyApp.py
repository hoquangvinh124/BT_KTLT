from PyQt6.QtWidgets import QApplication, QMainWindow

from E81.management_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()