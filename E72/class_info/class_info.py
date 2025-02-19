class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Trip:
    def __init__(self, trip_id, destination, price):
        self.trip_id = trip_id
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"{self.destination}, Price: {self.price}"

class Ticket:
    def __init__(self, ticket_id, passenger, trip):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.trip = trip

    def print_info(self):
        return f"ID: {self.ticket_id}, Passenger: {self.passenger.name}, Destination: {self.trip}"

    def print_ticket(self):
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Passenger: {self.passenger.name}\n"
                f"Destination: {self.trip.destination}\n"
                f"Price: {self.trip.price}\n")



class BookingSystem:
    def __init__(self):
        self.tickets = []
        self.revenue = 0

    def book_ticket(self, ticket_id, passenger, trip):
        ticket = Ticket(ticket_id, passenger, trip)
        self.tickets.append(ticket)
        self.revenue += trip.price
        return ticket

    def cancel_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                self.revenue -= ticket.trip.price
                self.tickets.remove(ticket)
                return True
        return False

    def total_revenue(self):
        return self.revenue

    def is_ticket_id_exit(self, ticket_id):
        for ticket in self.tickets:
            if ticket_id == ticket.ticket_id:
                return True
        return False

    def retrieve_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket_id == ticket.ticket_id:
                return ticket


def sample_trip():
    trips = [
        Trip(1, "Ho Chi Minh", 200),
        Trip(2, "Ha Noi", 250),
        Trip(3, "Da Nang", 180),
        Trip(4, "Hue", 300)
    ]
    return trips

