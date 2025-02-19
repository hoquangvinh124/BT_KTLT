from Product import Product
from Cagetory import Category

list = []
c1 = Category("c1", "Laptop")
c2 = Category("c2", "Phone")
c3 = Category("c3", "TV")
list.append(c1)
list.append(c2)
list.append(c3)

p1 = Product("p1", "DELL 1", 15, "TQ")
c1.add_product(p1)

p3 = Product("p3", "Samsung X1", 13, "TQ")
c2.add_product(p3)

for c in list:
    print("-" * 30)
    print(c)
    print("-" * 30)
    for p in c.list_products:
        print(p)
