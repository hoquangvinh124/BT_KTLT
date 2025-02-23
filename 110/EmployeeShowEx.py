
import csv
from EmployeeShow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.employees = []
        self.current_index = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.load_data()
        self.show_employee(0)
        self.pushButtonPrev.clicked.connect(self.show_prev_employee)
        self.pushButtonNext.clicked.connect(self.show_next_employee)
        self.pushButtonK.clicked.connect(self.show_first_employee)
        self.pushButtonK_2.clicked.connect(self.show_last_employee)
        self.pushButtonThem.clicked.connect(self.add_employee)
        self.pushButtonSua.clicked.connect(self.update_employee)
        self.pushButtonXoa.clicked.connect(self.delete_employee)
        self.pushButtonLuu.clicked.connect(self.clear_content)

    def load_data(self):
        with open('employee.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.employees.append(row)

    def show_employee(self, index):
        row = self.employees[index]
        self.lineEditMa.setText(row[0])
        self.lineEditTenNV.setText(row[1])
        self.lineEditDiaChi.setText(row[2])
        self.lineEditSDT.setText(row[3])
        self.lineEditQueQuan.setText(row[4])
        self.lineEditSoCMND.setText(row[5])
        self.lineEditNgayCap.setText(row[6])
        self.lineEditNoiCap.setText(row[7])
        self.labelRecord.setText(f"Record: {index+1}/{len(self.employees)}")

    def show_prev_employee(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_employee(self.current_index)

    def show_next_employee(self):
        if self.current_index < len(self.employees) - 1:
            self.current_index += 1
            self.show_employee(self.current_index)

    def show_first_employee(self):
        self.current_index = 0
        self.show_employee(self.current_index)

    def show_last_employee(self):
        self.current_index = len(self.employees) - 1
        self.show_employee(self.current_index)

    def save_data(self):
        with open('employee.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.employees)

    def add_employee(self):
        new_row = [
        self.lineEditMa.text(),
        self.lineEditTenNV.text(),
        self.lineEditDiaChi.text(),
        self.lineEditSDT.text(),
        self.lineEditQueQuan.text(),
        self.lineEditSoCMND.text(),
        self.lineEditNgayCap.text(),
        self.lineEditNoiCap.text()
        ]
        self.employees.append(new_row)
        self.current_index = len(self.employees) - 1
        self.show_employee(self.current_index)
        self.save_data()

    def update_employee(self):
        if 0 <= self.current_index < len(self.employees):
            updated_employee = [
                self.lineEditMa.text().strip(),
                self.lineEditTenNV.text().strip(),
                self.lineEditDiaChi.text().strip(),
                self.lineEditSDT.text().strip(),
                self.lineEditQueQuan.text().strip(),
                self.lineEditSoCMND.text().strip(),
                self.lineEditNgayCap.text().strip(),
                self.lineEditNoiCap.text().strip()
            ]
            self.employees[self.current_index] = updated_employee
            self.save_data()
            self.show_employee(self.current_index)

    def delete_employee(self):
        if 0 <= self.current_index < len(self.employees):
            del self.employees[self.current_index]
            if self.current_index >= len(self.employees):
                self.current_index = len(self.employees) - 1
            if self.current_index >= 0:
                self.show_employee(self.current_index)
            else:
                self.lineEditMa.clear()
                self.lineEditTenNV.clear()
                self.lineEditDiaChi.clear()
                self.lineEditSDT.clear()
                self.lineEditQueQuan.clear()
                self.lineEditSoCMND.clear()
                self.lineEditNgayCap.clear()
                self.lineEditNoiCap.clear()
                self.labelRecord.setText("Record: 0/0")
        self.save_data()

    def clear_content(self):
        self.lineEditMa.clear()
        self.lineEditTenNV.clear()
        self.lineEditDiaChi.clear()
        self.lineEditSDT.clear()
        self.lineEditQueQuan.clear()
        self.lineEditSoCMND.clear()
        self.lineEditNgayCap.clear()
        self.lineEditNoiCap.clear()
        self.lineEditMa.setFocus()

    def show(self):
        self.MainWindow.show()


