class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

class Product:
    def __init__(self, product_id, name, category, unit_price, manufacturer):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.manufacturer = manufacturer


