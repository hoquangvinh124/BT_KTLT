from PyQt6.QtWidgets import QApplication, QMainWindow

from E71.ui.BlueLock_Bank_Ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()