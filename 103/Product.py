class Product:
    def __init__(self, id, name, price, timetracking):
        self.id = id
        self.name = name
        self.price = price
        self.timetracking = timetracking

    def __str__(self):
        return f"{self.id}-{self.name} ({self.price} $)"
