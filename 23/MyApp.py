from PyQt6.QtWidgets import QApplication, QMainWindow

from Book_Selling_Ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()