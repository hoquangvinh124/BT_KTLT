from PyQt6.QtWidgets import QApplication, QMainWindow

from E68.ui.e_commerce_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()