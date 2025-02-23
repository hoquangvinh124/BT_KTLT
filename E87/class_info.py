class Customer:
    def __init__(self, code, name, phone, email):
        self.code = code
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.code}- {self.name}"

class Room:
    def __init__(self, code, name, room_type):
        self.code = code
        self.name = name
        self.room_type = room_type

    def __str__(self):
        return f"{self.code} - {self.name} - {self.room_type}"

class Booking:
    def __init__(self, customer_code, room_code, start_date, end_date):
        self.customer_code = customer_code
        self.room_code = room_code
        self.start_date = start_date
        self.end_date = end_date

