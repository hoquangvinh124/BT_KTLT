from PyQt6.QtWidgets import QApplication, QMainWindow

from TaskManagementEx import MainWindowEx

app=QApplication([])
window=MainWindowEx()
window.setupUi(QMainWindow())
window.show()
app.exec()