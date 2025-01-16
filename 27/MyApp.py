from PyQt6.QtWidgets import QApplication, QMainWindow

from Trinh_Tran_Phuong_Tuan_ex import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()