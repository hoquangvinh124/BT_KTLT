import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox
from Employeeclass import Employee
from Management import Ui_MainWindow
from pathlib import Path

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.data_set=[]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonNew.clicked.connect(self.process_new)
        self.pushButtonSave.clicked.connect(self.process_save)
        self.listWidgetEmployee.itemSelectionChanged.connect(self.process_item_selection_changed)
        self.pushButtonDelete.clicked.connect(self.process_delete)
        self.pushButtonClose.clicked.connect(self.process_close)
        self.read_employee_from_json()

    def process_new(self):
        self.lineEditName.setText("")
        self.lineEditEmail.setText("")
        self.lineEditName.setFocus()

    def process_save(self):
        name = self.lineEditName.text().strip()
        email = self.lineEditEmail.text().strip()
        gender = self.radWoman.isChecked()
        new_employee = Employee(name, email, gender)
        found_item = None
        for i in range(self.listWidgetEmployee.count()):
            item = self.listWidgetEmployee.item(i)
            existing_employee = item.data(Qt.ItemDataRole.UserRole)
            if new_employee.email.lower() == existing_employee.email.lower():
                found_item = item
                break
        if found_item:
            item = found_item
        else:
            item = QListWidgetItem()
            self.listWidgetEmployee.addItem(item)
        item.setData(Qt.ItemDataRole.UserRole, new_employee)
        item.setText(str(new_employee))
        item.setCheckState(Qt.CheckState.Unchecked)
        if new_employee.gender:
            item.setIcon(QIcon("images/ic_woman.png"))
        else:
            item.setIcon(QIcon("images/ic_man.png"))
        self.write_employee_to_json()

    def process_item_selection_changed(self):
        current_row = self.listWidgetEmployee.currentRow()
        if current_row < 0:
            return
        item = self.listWidgetEmployee.item(current_row)
        emp = item.data(Qt.ItemDataRole.UserRole)
        self.lineEditName.setText(emp.name)
        self.lineEditEmail.setText(emp.email)
        if emp.gender:
            self.radWoman.setChecked(True)
        else:
            self.radMan.setChecked(True)

    def process_delete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidgetEmployee.count()-1,-1,-1):
            item=self.listWidgetEmployee.item(index)
            if item.checkState()==Qt.CheckState.Checked:
                current_item = self.listWidgetEmployee.takeItem(index)
                del current_item
        self.process_new()
        self.write_employee_to_json()

    def process_close(self):
        msg = QMessageBox()
        msg.setText(f"Are you sure you want to exit ?")
        msg.setWindowTitle("Exit Confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.Yes:
           self.MainWindow.close()

    def write_employee_to_json(self):
        dataset=[]
        for i in range(0,self.listWidgetEmployee.count()):
            item=self.listWidgetEmployee.item(i)
            emp=item.data(Qt.ItemDataRole.UserRole)
            dataset.append(emp)
        json_string=json.dumps([emp.__dict__ for emp in dataset])
        json_file=open("employee.json", "w")
        json_file.write(json_string)
        json_file.close()

    def read_employee_from_json(self):
        json_path = Path("employee.json")
        if not json_path.is_file():
            return
        with json_path.open("r", encoding="utf-8") as file:
            self.data_set = json.load(file, object_hook=lambda d: Employee(**d))
        for emp in self.data_set:
            item = QListWidgetItem(str(emp))
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setCheckState(Qt.CheckState.Unchecked)
            icon_path = "images/ic_woman.png" if emp.gender else "images/ic_man.png"
            item.setIcon(QIcon(icon_path))

            self.listWidgetEmployee.addItem(item)

    def show(self):
        self.MainWindow.show()