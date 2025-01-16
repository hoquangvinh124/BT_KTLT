
from soft import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.add()
        self.comboBox.activated.connect(self.process_signal_combobox)

    def add(self):
        self.comboBox.addItems(['Laptop','Phone & Tablet','Smart Watch',
                                "Head Phone","Mouse","Mouse Pad","Game & Stream","Monitor"])

    def process_signal_combobox(self):
        index = self.comboBox.currentIndex()
        context = self.comboBox.currentText()
        self.label_2.setText(f"You selected index = {index}, text = {context}")

    def show(self):
        self.MainWindow.show()