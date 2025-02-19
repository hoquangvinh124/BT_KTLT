class Product:
    def __init__(self, product_id, product_name, price, expired_date, free_tax):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.expired_date = expired_date
        self.free_tax = free_tax

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"
