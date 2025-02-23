class Product:
    def __init__(self, id, name, price, file_path=None):
        self.id = id
        self.name = name
        self.price = price
        self.file_path = file_path

    def __str__(self):
        return f"{self.id} - {self.name} - ${self.price}"