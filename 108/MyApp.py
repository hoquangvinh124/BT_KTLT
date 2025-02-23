from PyQt6.QtWidgets import QApplication, QMainWindow

from SongEx import MainWindowEx

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()