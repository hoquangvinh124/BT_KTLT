from E87.lib.CSVFactory import CSVFileFactory
from E87.class_info import *
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMessageBox, QDialog, QHBoxLayout
from E87.ui.MainPage import Ui_MainWindow

class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ListCustomer = CSVFileFactory.read_data("../data/customer.csv", Customer)
        self.ListRoom = CSVFileFactory.read_data("../data/room.csv", Room)
        self.ListRoomReservation = CSVFileFactory.read_data("../data/book_reservation.csv", Booking)
        self.selected_customer = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.create_button(self.ListCustomer, self.ListRoom)
        self.pushButtonRemove.clicked.connect(lambda: self.cancel_booking(self.selected_customer))
        self.pushButtonSave.clicked.connect(self.save_booking)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def create_button(self, list_customer, list_rooms):
        self.clear_layout(self.verticalLayoutButton)
        self.room_buttons = {}

        for customer in list_customer:
            rowLayout = QHBoxLayout()
            btnCustomerInfo = QPushButton(str(customer))
            btnInfo = QPushButton("Info")
            btnBook = QPushButton("Book")
            btnInfo.clicked.connect(lambda _, c=customer: self.show_info(c))
            btnBook.clicked.connect(lambda _, c=customer: self.show_booking_detail(c))
            from PyQt6.QtWidgets import QSizePolicy
            btnCustomerInfo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            btnInfo.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
            btnInfo.setFixedWidth(60)
            btnInfo.setFixedHeight(40)
            btnBook.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
            btnBook.setFixedWidth(60)
            btnBook.setFixedHeight(40)
            rowLayout.addWidget(btnCustomerInfo)
            rowLayout.addWidget(btnInfo)
            rowLayout.addWidget(btnBook)
            self.verticalLayoutButton.addLayout(rowLayout)

        self.clear_layout(self.verticalLayoutButton_2)
        for room in list_rooms:
            rowLayout = QHBoxLayout()
            btnRoom = QPushButton(str(room))
            btnRoom.setObjectName(f"btnRoom_{room.code}")
            btnRoom.clicked.connect(lambda _, r=room: self.show_room(r))
            rowLayout.addWidget(btnRoom)
            self.verticalLayoutButton_2.addLayout(rowLayout)
            self.room_buttons[room.code] = btnRoom

    def show_room(self, r):
        self.lineEditName.setText(f"{r.code}")

    def show_booking_detail(self, customer):
        found_booking = None
        for booking in self.ListRoomReservation:
            if booking.customer_code == customer.code:
                found_booking = booking
                break
        if found_booking:
            room_code_str = found_booking.room_code
            btn = self.room_buttons.get(room_code_str)
            if btn:
                btn.setStyleSheet("background-color: pink;"
                                  "font-size: 16px;")
            self.lineEditId.setText(found_booking.customer_code)
            self.lineEditName.setText(found_booking.room_code)
            self.lineEditStart.setText(found_booking.start_date)
            self.lineEditEnd.setText(found_booking.end_date)
        else:
            for btn in self.room_buttons.values():
                btn.setStyleSheet("font-size: 16px;")
            self.lineEditId.clear()
            self.lineEditName.clear()
            self.lineEditStart.clear()
            self.lineEditEnd.clear()

    def show_info(self, customer):
        self.selected_customer = customer
        from E87.ui.DetailInfoEx import DetailInfoDialog
        dialog = DetailInfoDialog(customer)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            self.ListCustomer = CSVFileFactory.read_data("../data/customer.csv", Customer)
            self.create_button(self.ListCustomer, self.ListRoom)

    def cancel_booking(self, customer):
        found_index = None
        for i, booking in enumerate(self.ListRoomReservation):
            if booking.customer_code == customer.code:
                found_index = i
                break
        if found_index is not None:
            reply = QMessageBox.question(
                self,
                "Cancel Booking",
                "Are you sure to cancel?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                booking_to_cancel = self.ListRoomReservation.pop(found_index)
                CSVFileFactory.write_data(self.ListRoomReservation, "../data/book_reservation.csv")
                btn = self.room_buttons.get(booking_to_cancel.room_code)
                if btn:
                    btn.setStyleSheet("font-size: 16px;")
                self.lineEditId.clear()
                self.lineEditName.clear()
                self.lineEditStart.clear()
                self.lineEditEnd.clear()
                QMessageBox.information(self, "Cancel Booking", "Booking Canceled!")
        else:
            QMessageBox.information(self, "Cancel Booking", "Booking not found to cancel!")

    def save_booking(self):
        customer_code = self.lineEditId.text()
        room_code = self.lineEditName.text()
        start_date = self.lineEditStart.text()
        end_date = self.lineEditEnd.text()
        new_booking = Booking(customer_code, room_code, start_date, end_date)
        self.ListRoomReservation.append(new_booking)
        CSVFileFactory.write_data(self.ListRoomReservation, "../data/book_reservation.csv")
        btn = self.room_buttons.get(room_code)
        if btn:
            btn.setStyleSheet("background-color: pink;")
        QMessageBox.information(self, "Success","Save Reservation Success")

    def show(self):
        self.MainWindow.show()