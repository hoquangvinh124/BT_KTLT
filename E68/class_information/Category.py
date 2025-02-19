class Category:
    def __init__(self, category_id, name, description=""):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return f"Category[ID={self.category_id}, {self.name}]"
