from QTableWidget import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.tableWidget.itemSelectionChanged.connect(self.processSelectedItem)

    def processSelectedItem(self):
        row = self.tableWidget.currentRow()
        songId = self.tableWidget.item(row,0)
        songName = self.tableWidget.item(row,1)
        singer = self.tableWidget.item(row,2)
        self.lineEdit.setText(songId.text())
        self.lineEdit_2.setText(songName.text())
        self.lineEdit_3.setText(singer.text())

    def show(self):
        self.MainWindow.show()