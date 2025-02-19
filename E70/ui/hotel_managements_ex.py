from E70.ui.hotel_managements import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMessageBox
from E70.class_info.class_info import *
from datetime import *

class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.rooms, self.customer, self.bookings = sample_data()
        self.booking_list = [o for o in self.bookings]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.add_booking)
        self.pushButton_2.clicked.connect(self.remove_by_id)
        self.set_combobox_info()
        self.create_button(self.booking_list)
        self.pushButton_4.clicked.connect(self.show_invoice)
        self.pushButton_3.clicked.connect(self.calculate_fee)

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
        for booking in list:
            btn = QPushButton(booking.get_info())
            btn.clicked.connect(lambda _, b=booking: self.show_orders_details(b))
            self.verticalLayoutButton.addWidget(btn)

    def show_orders_details(self, b):
        self.lineEdit.setText(f"{b.booking_id}")
        self.lineEdit_2.setText(f"{b.customer.name}")
        self.lineEdit_3.setText(f"{b.customer.contact_info}")
        date_not_format = b.check_in_date
        self.lineEdit_4.setText(date_not_format.strftime("%d-%m-%Y"))
        date_not_format = b.check_out_date
        self.lineEdit_5.setText(date_not_format.strftime("%d-%m-%Y"))
        self.comboBox.setCurrentText(b.room.get_info())

    def add_booking(self):
        booking_id = self.lineEdit.text()
        customer = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        checkin = datetime.strptime(self.lineEdit_4.text(), "%d-%m-%Y")
        checkout = datetime.strptime(self.lineEdit_5.text(), "%d-%m-%Y")
        room_type = self.comboBox.currentData()
        exist = False
        for booking in self.booking_list:
            if booking_id == str(booking.booking_id):
                exist = True
                print("Ban phai xoa booking cu truoc khi them (trung id)")
        if not exist:
            if room_type.is_available:
                self.booking_list.append(Booking(booking_id, customer, phone, room_type, checkin, checkout))
                room_type.book()
            else:
                print("Phong da co nguoi dat")
        self.create_button(self.booking_list)

    def remove_by_id(self):
        booking_id = str(self.lineEdit.text())
        success = False
        for i, b in enumerate(self.booking_list):
            if str(b.booking_id) == booking_id:
                self.booking_list.pop(i)
                success = True
                current_room = self.comboBox.currentData()
                current_room.cancel_booking()
        if not success:
            print("ID Booking k tim thay de tra phong")
        self.create_button(self.booking_list)

    def set_combobox_info(self):
        for room in self.rooms:
            self.comboBox.addItem(room.get_info(), room)

    def show_invoice(self):
        booking = None
        booking_id = str(self.lineEdit.text())
        found = False
        for b in self.booking_list:
            if str(b.booking_id) == booking_id:
                booking = b
                found = True
                break
        if found:
            invoice_text = (
                f"Hotel Invoice\n"
                f"Booking ID: {booking.booking_id}\n"
                f"Customer: {booking.customer.name}\n"
                f"Phone number: {booking.customer.contact_info}\n"
                f"Total: {booking.total_price:,} VND\n"
                f"----------------------\n"
                f"Thank you for choosing our service!"
            )
            QMessageBox.information(self, "Invoice", invoice_text)
        else:
            QMessageBox.warning(self, "Error", "Please choose current booking to continue!")

    def calculate_fee(self):
        booking = None
        booking_id = str(self.lineEdit.text())
        found = False
        for b in self.booking_list:
            if str(b.booking_id) == booking_id:
                booking = b
                found = True
                break
        if found:
            text = (
                f"Booking ID: {booking.booking_id}\n"
                f"Customer: {booking.customer.name}\n"
                f"Phone number: {booking.customer.contact_info}\n"
                f"{booking.room.get_info()}\n"
                f"Price per night: {booking.room.price}\n"
                f"Total Fee: {booking.total_price:,} VND\n"
            )
            QMessageBox.information(self, "Fee", text)
        else:
            QMessageBox.warning(self, "Error", "Please choose current booking to continue!")

    def show(self):
        self.MainWindow.show()


