from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QInputDialog
from E81.management import Ui_MainWindow
from E81.utils import *

class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.create_button(read_employee("employee.xml"))
        self.pushButton.clicked.connect(self.change_information)
        self.pushButton_2.clicked.connect(self.remove_by_id)
        self.pushButton_3.clicked.connect(self.search_id)
        self.pushButton_5.clicked.connect(self.sort_employee)

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
            btn = QPushButton(emp.__str__())
            btn.clicked.connect(lambda _, e=emp: self.show_emp_details(e))
            self.verticalLayoutButton.addWidget(btn)

    def show_emp_details(self, e):
        self.lineEdit.setText(f"{e.id}")
        self.lineEdit_2.setText(f"{e.name}")

    def change_information(self):
        id = self.lineEdit.text()
        name = self.lineEdit_2.text()
        find_to_edit_or_insert("employee.xml", id, name)
        self.create_button(read_employee("employee.xml"))

    def remove_by_id(self):
        id = str(self.lineEdit.text())
        try:
            remove_employee("employee.xml", id)
        except ValueError:
            print("Not found ID to delete")
        self.create_button(read_employee("employee.xml"))


    def sort_employee(self):
        data = read_employee("employee.xml")
        data.sort(key=lambda e: e.name.split()[-1].lower())
        self.create_button(data)

    def search_id(self):
        id, ok = QInputDialog.getText(self, "Search By ID", "Please Input ID")
        if ok:
            data = search_id("employee.xml", id)
            self.create_button(data)

    def show(self):
        self.MainWindow.show()