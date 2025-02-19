class Product:

    def __init__(self, product_id , product_name, unit_price):
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price

    def get_info(self):
        return f"{self.product_id}\t{self.product_name}\t{self.unit_price}"