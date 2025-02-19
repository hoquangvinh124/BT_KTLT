from Category import Category
from Product import Product

class Dataset:
    def __init__(self, categories=None):
        self.categories = categories if categories is not None else []

    def item(self, index):
        return self.categories[index]

    def add(self, c):
        self.categories.append(c)

    def add_all(self, categories):
        self.categories.extend(categories)

    def index(self, c):
        return self.categories.index(c)

    def update(self, index, c):
        self.categories[index] = c
        return self.categories[index]

    def remove_by_index(self, index):
        return self.categories.pop(index)

    def remove_by_item(self, item):
        self.categories.remove(item)

    def clear(self):
        self.categories.clear()

    def size(self):
        return len(self.categories)

    def print_all(self):
        for category in self.categories:
            print(category)
            for product in category.products:
                print(product)

    def re_model(self):
        self.categories = [
            Category(
                dict_c["id"],
                dict_c["name"],
                [
                    Product(dict_p["id"], dict_p["name"], dict_p["price"], dict_p["timetracking"])
                    for dict_p in dict_c["products"]
                ]
            )
            for dict_c in self.categories
        ]
