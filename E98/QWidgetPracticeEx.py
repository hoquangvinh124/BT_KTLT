from QWidgetPractice import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.btn_double.clicked.connect(self.increment_double)
        self.btn_highlight_even.clicked.connect(self.highlight_even)
        self.btn_highlight_odd.clicked.connect(self.highlight_odd)
        self.btn_remove_ends.clicked.connect(self.remove_first_last)
        self.btn_remove_selected.clicked.connect(self.remove_selected)
        self.btn_square.clicked.connect(self.change_to_square)
        self.btn_sum.clicked.connect(self.sum_numbers)
        self.update_button.clicked.connect(self.update)

    def update(self):
        number = float(self.number_input.text())
        self.numbers_list.addItem(str(number))

    def sum_numbers(self):
        total = sum(float(self.numbers_list.item(i).text())
                    for i in range(self.numbers_list.count()))
        QMessageBox.information(self.MainWindow, "Sum", f"Sum of all numbers: {total}")

    def remove_first_last(self):
        if self.numbers_list.count() >= 2:
            self.numbers_list.takeItem(self.numbers_list.count() - 1)
            self.numbers_list.takeItem(0)

    def remove_selected(self):
        current = self.numbers_list.currentRow()
        if current != -1:
            self.numbers_list.takeItem(current)

    def increment_double(self):
        for i in range(self.numbers_list.count()):
            current_value = float(self.numbers_list.item(i).text())
            new_value = current_value * 2
            self.numbers_list.item(i).setText(str(new_value))

    def change_to_square(self):
        current = self.numbers_list.currentRow()
        if current != -1:
            value = float(self.numbers_list.item(current).text())
            self.numbers_list.item(current).setText(str(value * value))

    def highlight_even(self):
        for i in range(self.numbers_list.count()):
            value = float(self.numbers_list.item(i).text())
            if value % 2 == 0:
                self.numbers_list.item(i).setBackground(Qt.GlobalColor.yellow)
            else:
                self.numbers_list.item(i).setBackground(Qt.GlobalColor.white)

    def highlight_odd(self):
        for i in range(self.numbers_list.count()):
            value = float(self.numbers_list.item(i).text())
            if value % 2 != 0:
                self.numbers_list.item(i).setBackground(Qt.GlobalColor.yellow)
            else:
                self.numbers_list.item(i).setBackground(Qt.GlobalColor.white)

    def show(self):
        self.MainWindow.show()