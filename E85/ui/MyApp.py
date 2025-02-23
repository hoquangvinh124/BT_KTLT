from PyQt6.QtWidgets import QApplication, QMainWindow

from E85.ui.LoginEx import LoginMainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowEx()
myui.setupUi(mainwindow)
myui.show()
app.exec()