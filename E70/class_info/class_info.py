from datetime import date
class Room:
    def __init__(self, room_number, room_type, price, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available

    def book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def cancel_booking(self):
        self.is_available = True

    def get_info(self):
        return f"Room Number: {self.room_number}, {self.room_type}"


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Booking:
    def __init__(self, booking_id, name, phone, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.customer = Customer(name, phone)
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = self.calculate_total()

    def calculate_total(self):
        num_days = (self.check_out_date - self.check_in_date).days
        return num_days * self.room.price

    def cancel(self):
        self.room.cancel_booking()
        return f"Booking {self.booking_id} cancelled."

    def get_info(self):
        return f"ID:{self.booking_id}, Customer:{self.customer.name}, Phone:{self.customer.contact_info}"


def sample_data():
    rooms = [
        Room(101, "Standard", 500_000),
        Room(102, "Deluxe", 800_000),
        Room(103, "Suite", 1_500_000)
    ]

    customers = [
        Customer("Nguyễn Văn A", "0987654321"),
        Customer("Trần Thị B", "0976543210"),
        Customer("Lê Văn C", "0965432109")
    ]

    bookings = [
        Booking(1, customers[0].name, customers[0].contact_info, rooms[0], date(2025, 2, 10), date(2025, 2, 15))
    ]
    rooms[0].book()
    return rooms, customers, bookings