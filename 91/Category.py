class Category:
    def __init__(self,id=None,name=None,products=None):
        if products==None:
            self.products=[]
        else:
            self.products=products
        self.id=id
        self.name=name

    def __str__(self):
        return f"{self.id}\t{self.name}"

    def addProduct(self,product):
        self.products.append(product)
        
    def printProducts(self):
        for product in self.products:
            print(product)