class Category:
    def __init__(self, cate_id, cate_name):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.list_products = []

    def __str__(self):
        infor = f"{self.cate_id}\t{self.cate_name}"
        return infor

    def add_product(self, p):
        self.list_products.append(p)

    def print_products(self):
        for p in self.list_products:
            print(p)
