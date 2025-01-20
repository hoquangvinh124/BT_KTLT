from E60.class_student import *
from E60.class_student.student import StudentManagement, Student
from manage_students import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLineEdit, QDialog, QLabel, QDialogButtonBox, QWidget
from datetime import datetime

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.list_of_students = StudentManagement()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.create_button(self.list_of_students.return_array())
        self.pushButton.clicked.connect(self.change_information)
        self.pushButton_3.clicked.connect(self.search_full_name)
        self.pushButton_5.clicked.connect(self.search_current_month)
        self.pushButton_4.clicked.connect(self.sort_student)
        self.pushButton_6.clicked.connect(self.sort_student_desc)
        self.pushButton_2.clicked.connect(self.remove_student)

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
        for student in list:
            btn = QPushButton(student.print_information())
            btn.clicked.connect(lambda _, s=student: self.show_student_details(s))
            self.verticalLayoutButton.addWidget(btn)

    def show_student_details(self, student):
        self.lineEdit.setText(f"{student.student_id}")
        self.lineEdit_2.setText(f"{student.full_name}")
        self.lineEdit_3.setText(f"{student.first_name}")
        self.lineEdit_4.setText(f"{student.last_name}")
        dob = student.date_of_birth
        formatted_date = dob.strftime("%d-%m-%Y")
        self.lineEdit_5.setText(f"{formatted_date}")
        self.lineEdit_6.setText(f"{student.age}")

    def change_information(self):
        id_student = str(self.lineEdit.text())
        full_name = str(self.lineEdit_2.text())
        dob = str(self.lineEdit_5.text())
        try:
            date_of_birth = datetime.strptime(dob, "%d-%m-%Y")
            found = False
            for student in self.list_of_students.return_array():
                if student.student_id == id_student:
                    student.student_id = id_student
                    student.full_name = full_name
                    student.date_of_birth = date_of_birth
                    found = True
            if not found:
                obj = Student(id_student, full_name, dob)
                self.list_of_students.add_student(obj)
            self.create_button(self.list_of_students.return_array())
        except ValueError:
            print("Ngay sinh loi dinh dang (d-m-y)")

    def open_input_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Information")
        dialog.setModal(True)

        layout = QVBoxLayout()

        label = QLabel("Enter information: ")
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(buttons)
        dialog.setLayout(layout)
        user_input = ""

        def on_accept():
            nonlocal user_input
            user_input = input_field.text()
            dialog.accept()
        buttons.accepted.connect(on_accept)
        buttons.rejected.connect(dialog.reject)
        dialog.exec()
        return user_input

    def search_full_name(self):
        full_name = self.open_input_dialog()
        self.create_button(self.list_of_students.find_students_by_name(full_name))

    def search_current_month(self):
        self.create_button(self.list_of_students.find_students_with_birthday_in_current_month())

    def sort_student(self):
        self.create_button(self.list_of_students.sort_students_by_age())

    def sort_student_desc(self):
        self.create_button(self.list_of_students.sort_students_by_age_desc())

    def remove_student(self):
        student_id = str(self.lineEdit.text())
        self.create_button(self.list_of_students.remove_by_id(student_id))

    def show(self):
        self.MainWindow.show()