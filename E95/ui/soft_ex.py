from PyQt6.QtGui import QIcon
from soft import Ui_MainWindow
from E95.object.class_category import Category

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.comboBox.activated.connect(self.process_selected_combobox)

        fb_icon = QIcon(r"\E95\images\fb.png")
        fb = Category(1, "Facebook")
        self.comboBox.addItem(fb_icon, fb.name, fb)

        insta_icon = QIcon("/E95/images/insta.png")
        insta = Category(2, "Instagram")
        self.comboBox.addItem(insta_icon, insta.name, insta)

        threads_icon = QIcon("E95/images/threads.png")
        threads = Category(3, "Threads")
        self.comboBox.addItem(threads_icon, threads.name, threads)

        x_icon = QIcon("E95/images/x.png")
        x = Category(4, "X")
        self.comboBox.addItem(x_icon, x.name, x)

    def process_selected_combobox(self):
        data = self.comboBox.currentData()
        self.label_2.setText(
            f'You selected index= {data}')

    def show(self):
        self.MainWindow.show()

