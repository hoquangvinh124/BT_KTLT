from E96.libs.employee_class import Employee
from AduASen import Ui_MainWindow
from PyQt6.QtGui import QIcon

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        hcm = QIcon(r"../images/ic_hochiminh.PNG")
        self.comboBox.addItem(hcm, "Ho Chi Minh")

        hue = QIcon(r"../images/ic_hue.PNG")
        self.comboBox.addItem(hue, "Hue")

        ha_noi= QIcon(r"../images/ic_hanoi.PNG")
        self.comboBox.addItem(ha_noi, "Ha Noi")

        da_nang = QIcon(r"../images/ic_danang.PNG")
        self.comboBox.addItem(da_nang, "Da Nang")

        da_lat = QIcon(r"../images/ic_dalat.PNG")
        self.comboBox.addItem(da_lat, "Da Lat")

        can_tho = QIcon(r"../images/ic_cantho.PNG")
        self.comboBox.addItem(can_tho, "Can Tho")

        self.pushButton_2.clicked.connect(self.processClose)
        self.pushButton.clicked.connect(self.processConfirmation)

    def processConfirmation(self):
        name = self.lineEdit.text()
        gender = "Man"
        if self.checkBox.isChecked():
            gender="Woman"
        city = self.comboBox.currentText()
        emp = Employee(name,gender,city)
        self.plainTextEdit.setPlainText(str(emp))

    def processClose(self):
        self.MainWindow.close()

    def show(self):
        self.MainWindow.show()