class Product:
    def __init__(self, product_id, product_name, category_id, unit_price, quantity, discount=0.0):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.unit_price = unit_price
        self.quantity = quantity
        self.discount = discount

    def __str__(self):
        return (f"Product[ID={self.product_id}, {self.product_name}, "
                f"UnitPrice={self.unit_price}, "
                f"Quantity={self.quantity}, Discount={self.discount}]")