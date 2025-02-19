from E80.FileFactory import FileFactory
from E80.Product import Product

print("Input Products:")
while True:
    product_id = input("Input Product ID:")
    product_name = input("Input Product Name:")
    unit_price = float(input("Input Unit Price:"))
    product = Product(product_id, product_name, unit_price)

    FileFactory.write_data("database.txt", product)
    ans = input("Continue?(Y/N):")
    if ans != 'Y' or ans != 'y':
        break

