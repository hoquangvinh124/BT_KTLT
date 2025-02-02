class Product:
    def __init__(self, product_id, product_name, price, madein):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.madein = madein

    def __str__(self):
        info = f"{self.product_id}\t{self.product_name}\t{self.price}\t{self.madein}"
        return info
