from PyQt6.QtWidgets import QApplication, QMainWindow

from Ex99_ui import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()