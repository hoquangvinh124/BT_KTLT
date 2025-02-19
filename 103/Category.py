class Category:
    def __init__(self, id, name, products=None):
        self.id = id
        self.name = name
        self.products = products if products is not None else []

    def item(self, index):
        return self.products[index]

    def add(self, p):
        self.products.append(p)

    def addAll(self, products):
        self.products.extend(products)

    def index(self, p):
        return self.products.index(p)

    def update(self, index, p):
        self.products[index] = p
        return self.products[index]

    def removeByIndex(self, index):
        return self.products.pop(index)

    def removeByItem(self, item):
        self.products.remove(item)

    def clear(self):
        self.products.clear()

    def size(self):
        return len(self.products)

    def __str__(self):
        return f"{self.id}-{self.name}"
