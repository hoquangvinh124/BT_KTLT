from employee import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QInputDialog, QWidget
from class_info import *

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.list_of_employee = ListOfEmployee()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.change_information)
        self.pushButton_2.clicked.connect(self.remove_employee)
        self.pushButton_3.clicked.connect(self.search_id_card)
        self.pushButton_5.clicked.connect(self.filter_dob)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def create_button(self, list):
        self.clear_layout(self.verticalLayoutButton)
        for emp in list:
            btn = QPushButton(emp.display_info())
            if isinstance(emp, OfficialEmployee):
                btn.setStyleSheet("background-color: yellow")
            btn.clicked.connect(lambda _, e=emp: self.show_employee_details(e))
            self.verticalLayoutButton.addWidget(btn)

    def show_employee_details(self, e):
        self.lineEdit.setText(f"{e.id}")
        self.lineEdit_2.setText(f"{e.name}")
        self.lineEdit_3.setText(f"{e.id_card}")
        dob = e.birthday
        formatted_date = dob.strftime("%d-%m-%Y")
        self.lineEdit_5.setText(f"{formatted_date}")

    def change_information(self):
        id = str(self.lineEdit.text())
        name = str(self.lineEdit_2.text())
        id_card = str(self.lineEdit_3.text())
        dob = str(self.lineEdit_5.text())
        try:
            date_of_birth = datetime.strptime(dob, "%d-%m-%Y")
            found = False
            for e in self.list_of_employee.arr:
                if e.id == id:
                    e.id = id
                    e.name = name
                    e.id_card = id_card
                    e.date_of_birth = date_of_birth
                    found = True
            if not found:
                if self.checkBox.isChecked():
                    obj = OfficialEmployee(id, name, id_card, dob)
                    self.list_of_employee.add_employee(obj)
                else:
                    obj = TemporaryEmployee(id, name, id_card, dob, 0)
                    self.list_of_employee.add_employee(obj)
            self.create_button(self.list_of_employee.arr)
        except ValueError as e:
            print(e)
            print("Ngay sinh loi dinh dang (d-m-y)")

    def search_id_card(self):
        id_card, confirm = QInputDialog.getText(self.MainWindow, "Enter ID Card", "Enter ID Card:")
        if confirm:
            self.create_button(self.list_of_employee.search_id_card(id_card))

    def filter_dob(self):
        year, confirm = QInputDialog.getText(self.MainWindow, "Enter year", "Enter year:")
        if confirm:
            self.create_button(self.list_of_employee.filter_by_dob(year))

    def remove_employee(self):
        id = self.lineEdit.text()
        self.create_button(self.list_of_employee.remove_employee(id))

    def show(self):
        self.MainWindow.show()