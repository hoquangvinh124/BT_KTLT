class OrderDetail:
    def __init__(self, orderID, productID, unitPrice, quantity, discount=0.0):
        self.orderID = orderID
        self.productID = productID
        self.unitPrice = unitPrice
        self.quantity = quantity
        self.discount = discount

    def __str__(self):
        return (f"OrderDetail[OrderID={self.orderID}, ProductID={self.productID}, "
                f"UnitPrice={self.unitPrice}, Quantity={self.quantity}, "
                f"Discount={self.discount}]")
