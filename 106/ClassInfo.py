class Product:
    def __init__(self, id, name, manufacturer, price):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

    def __str__(self):
        return f"{self.id} - {self.name} - ${self.price}"


class ListOfProduct:
    def __init__(self):
        self.arr = []

    def add_product(self, product):
        self.arr.append(product)

    def remove_product(self, code):
        success = False
        for i, product in enumerate(self.arr):
            if product.id == code:
                self.arr.pop(i)
                success = True
        if not success:
            print("Code not found to delete")
        return self.arr

