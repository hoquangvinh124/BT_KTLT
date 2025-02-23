from PyQt6.QtWidgets import QApplication, QMainWindow

from E87.ui.MainPageEx import MainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowEx()
myui.setupUi(mainwindow)
myui.show()
app.exec()