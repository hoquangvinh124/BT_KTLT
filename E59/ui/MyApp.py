from PyQt6.QtWidgets import QApplication, QMainWindow

from ka_ku_la_to_ext import MainWindowExt

app=QApplication([])
myWindow= MainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()