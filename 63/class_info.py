class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.discount = 0
        self.tax = 0

    def calculate_final_price(self):
        discounted_price = float(self.price) * (1 - self.discount / 100.0)
        final_price = discounted_price * (1 + self.tax / 100.0)
        return final_price

    def display_info(self):
        return f"{self.code} - {self.name} - {self.price}"


class OfficialProduct(Product):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)
        self.tax = 10

class NonOfficialProduct(Product):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)
        self.discount = 10

class ListOfProduct:
    def __init__(self):
        self.arr = []

    def add_product(self, product):
        self.arr.append(product)

    def filter_price(self, price):
        filtered_price = [product for product in self.arr if product.calculate_final_price() <= price]
        return filtered_price

    def remove_product(self, code):
        success = False
        for i, product in enumerate(self.arr):
            if product.code == code:
                self.arr.pop(i)
                success = True
        if not success:
            print("Code not found to delete")
        return self.arr

    def search_name(self, name):
        filtered_product = [product for product in self.arr if name.lower() in product.name]
        return filtered_product