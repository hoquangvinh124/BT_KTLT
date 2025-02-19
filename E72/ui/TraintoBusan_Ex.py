from E72.ui.TraintoBusan import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QDialog, QLabel
from E72.class_info.class_info import *

class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.Train = BookingSystem()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.add_booking)
        self.pushButton_2.clicked.connect(self.remove_by_id)
        self.create_button(self.Train.tickets)
        self.pushButton_7.clicked.connect(self.print_ticket)
        self.display_trip()
        self.pushButton_3.clicked.connect(self.show_revenue)


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
        for ticket in list:
            btn = QPushButton(ticket.print_info())
            btn.clicked.connect(lambda _, t=ticket: self.show_ticket_details(t))
            self.verticalLayoutButton.addWidget(btn)

    def show_ticket_details(self, t):
        self.lineEdit.setText(f"{t.ticket_id}")
        self.lineEdit_2.setText(f"{t.passenger.name}")
        self.lineEdit_3.setText(f"{t.passenger.age}")
        self.comboBox.setCurrentText(t.trip.__str__())

    def add_booking(self):
        ticket_id = str(self.lineEdit.text())
        name = str(self.lineEdit_2.text())
        age = str(self.lineEdit_3.text())
        destination = self.comboBox.currentData()
        if self.Train.is_ticket_id_exit(ticket_id) or ticket_id == '':
            print("Da co ve ton tai voi ID nay/Khong bo trong ID")
        else:
            customer = Passenger(name, age)
            self.Train.book_ticket(ticket_id, customer, destination)
            self.create_button(self.Train.tickets)

    def remove_by_id(self):
        ticket_id = str(self.lineEdit.text())
        if not self.Train.is_ticket_id_exit(ticket_id):
            print("ID khong hop le de cancel ticket")
        else:
            self.Train.cancel_ticket(ticket_id)
        self.create_button(self.Train.tickets)

    def print_ticket(self):
        ticket_id = str(self.lineEdit.text())
        if self.Train.is_ticket_id_exit(ticket_id):
            dialog = QDialog()
            dialog.setWindowTitle("Ticket Info")
            layout = QVBoxLayout()
            ticket = self.Train.retrieve_ticket(ticket_id)
            info = ticket.print_ticket()
            label = QLabel(f"Ticket Info:\n{info}")
            layout.addWidget(label)
            dialog.setLayout(layout)
            dialog.exec()

    def display_trip(self):
        for t in sample_trip():
            self.comboBox.addItem(t.__str__(), t)

    def show_revenue(self):
        dialog = QDialog()
        dialog.setWindowTitle("Revenue")
        layout = QVBoxLayout()
        info = self.Train.total_revenue()
        label = QLabel(f"Total Revenue:\n{info}")
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec()

    def show(self):
        self.MainWindow.show()


