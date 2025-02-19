from E68.class_information.Category import Category
from E68.class_information.Customer import Customer
from E68.class_information.Employee import Employee
from E68.class_information.Order import Order
from E68.class_information.OrderDetail import OrderDetail
from E68.class_information.Product import Product

def create_sample_data():
    cat1 = Category(1, "Thiết bị điện tử", "Thiết bị điện tử")
    cat2 = Category(2, "Thời trang", "Thời trang")
    cat3 = Category(3, "Thực phẩm", "Thực phẩm")

    p1 = Product(101, "iPhone", cat1.category_id, 1000, 50, discount=0.1)
    p2 = Product(102, "Laptop Dell", cat1.category_id, 1500, 30, discount=0.05)
    p3 = Product(103, "Tai nghe", cat1.category_id, 200, 100, discount=0.15)
    p4 = Product(201, "Áo sơ mi", cat2.category_id, 25, 200)
    p5 = Product(202, "Quần jeans", cat2.category_id, 40, 150, discount=0.05)
    p6 = Product(203, "Giày thể thao", cat2.category_id, 60, 80, discount=0.1)
    p7 = Product(301, "Bánh ngọt", cat3.category_id, 5, 500)
    p8 = Product(302, "Nước ngọt", cat3.category_id, 2, 1000)
    p9 = Product(303, "Trà sữa", cat3.category_id, 3, 300)
    p10 = Product(304, "Mì gói", cat3.category_id, 1, 1000)


    for p in [p1, p2, p3]:
        cat1.add_product(p)
    for p in [p4, p5, p6]:
        cat2.add_product(p)
    for p in [p7, p8, p9, p10]:
        cat3.add_product(p)

    e1 = Employee(1, "Stark", "Tony", "Sales", "ironman", "pass123")
    e2 = Employee(2, "Rogers", "Steve", "Support", "captain", "pass234")
    e3 = Employee(3, "Parker", "Peter", "Manager", "spiderman", "pass345")
    e4 = Employee(4, "Romanoff", "Natasha", "Admin", "blackwidow", "pass456")

    c1 = Customer(1, "Dragneel", "Natsu", "Fairy Tail Guild", "Magnolia", "natsu", "dragonfire")
    c2 = Customer(2, "Scarlet", "Erza", "Fairy Tail Guild", "Magnolia", "erza", "requipe")
    c3 = Customer(3, "Fullbuster", "Gray", "Fairy Tail Guild", "Magnolia", "gray", "iceshield")
    c4 = Customer(4, "Heartfilia", "Lucy", "Fairy Tail Guild", "Magnolia", "lucy", "celestialkeys")
    c5 = Customer(5, "Fernandes", "Jellal", "Independent", "Unknown", "jellal", "heavenlybody")

    o1 = Order(1001, c1.customerID, e1.employeeID)
    od1_1 = OrderDetail(o1.orderID, p1.product_id, p1.unit_price, 2, p1.discount)
    od1_2 = OrderDetail(o1.orderID, p4.product_id, p4.unit_price, 3, p4.discount)
    o1.add_order_detail(od1_1)
    o1.add_order_detail(od1_2)

    o2 = Order(1002, c2.customerID, e2.employeeID)
    od2_1 = OrderDetail(o2.orderID, p2.product_id, p2.unit_price, 1, p2.discount)
    od2_2 = OrderDetail(o2.orderID, p7.product_id, p7.unit_price, 10, p7.discount)
    o2.add_order_detail(od2_1)
    o2.add_order_detail(od2_2)

    categories = [cat1, cat2, cat3]
    products = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    employees = [e1, e2, e3, e4]
    customers = [c1, c2, c3, c4, c5]
    orders = [o1, o2]

    return categories, products, employees, customers, orders