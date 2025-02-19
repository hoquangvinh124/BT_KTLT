from PyQt6.QtWidgets import QApplication, QMainWindow

from E70.ui.hotel_managements_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()