from PyQt6.QtWidgets import QTableWidgetItem

from Song import Ui_MainWindow
from XMLHandle import *

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
       self.data = MusicManager()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.data.load_songs()
        self.data.load_singers()
        self.load_info_to_box()
        self.comboBox.activated.connect(self.load_data_table_widget)

    def load_info_to_box(self):
        self.comboBox.addItems(self.data.get_singer_list())

    def load_data_table_widget(self):
        singer = self.comboBox.currentText()
        self.tableWidget.setRowCount(len(self.data.get_songs_by_singer(singer)))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Tên Bài Hát", "Sáng tác", "Rapper"])
        for i, s in enumerate(self.data.get_songs_by_singer(singer)):
            song = QTableWidgetItem(s[0])
            composer = QTableWidgetItem(s[1])
            rapper = QTableWidgetItem(singer)
            self.tableWidget.setItem(i, 0, song)
            self.tableWidget.setItem(i, 1, composer)
            self.tableWidget.setItem(i, 2, rapper)

    def show(self):
        self.MainWindow.show()