from PyQt6.QtWidgets import QApplication, QMainWindow

from lucky_game_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()