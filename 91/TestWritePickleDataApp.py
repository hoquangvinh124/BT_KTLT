from Category import Category
from FileUtil import FileUtil
from Product import Product

dataset=[]

cate1 = Category("cate1", "Electronic")
cate1.addProduct(Product("p1", "Light X", 100))
cate1.addProduct(Product("p2", "Fan X", 200))
cate1.addProduct(Product("p3", "MIC Z", 150))

print("Cate 1 information:")
print(cate1)
print("-"*15)
cate1.printProducts()
print("-"*15)

dataset.append(cate1)

cate2 = Category("cate2", "Houseware")
cate2.addProduct(Product("p4", "Bowl", 20))
cate2.addProduct(Product("p5", "Knife", 10))
cate2.addProduct(Product("p6", "Pan", 80))

print("Cate 2 information:")
print(cate2)
print("-"*15)
cate2.printProducts()
print("-"*15)

dataset.append(cate2)

print("All Categories:")
for cate in dataset:
    cate.printProducts()

ret = FileUtil.savemodel(dataset, "mydataset.data")
if ret:
    print("Save Pickle File successful!")
