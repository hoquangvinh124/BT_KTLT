from PyQt6.QtWidgets import QApplication, QMainWindow

from s_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()