class Order:
    def __init__(self, orderID, customerID, employeeID):
        self.orderID = orderID
        self.customerID = customerID
        self.employeeID = employeeID
        self.orderDetails = []

    def add_order_detail(self, od):
        self.orderDetails.append(od)

    def __str__(self):
        return (f"Order[ID={self.orderID}, CustomerID={self.customerID}, "
                f"EmployeeID={self.employeeID}]")

    def print_information(self):
        return f"ID:{self.orderID}, Customer ID:{self.customerID}, EmployeeID:{self.employeeID}"

