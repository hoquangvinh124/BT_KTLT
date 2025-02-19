class Customer:
    def __init__(self, customerID, contactName, contactTitle, address, city, userName, password):
        self.customerID = customerID
        self.contactName = contactName
        self.contactTitle = contactTitle
        self.address = address
        self.city = city
        self.userName = userName
        self.password = password

    def get_info(self):
        return f"ID: {self.customerID}, {self.contactTitle}"

    def __str__(self):
        return f"Customer[ID: {self.customerID}, Name: {self.contactTitle}, City: {self.city}, Username: {self.userName}]"