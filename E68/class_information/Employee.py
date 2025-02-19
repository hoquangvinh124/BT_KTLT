class Employee:
    def __init__(self, employeeID, lastName, firstName, role, userName, password):
        self.employeeID = employeeID
        self.lastName = lastName
        self.firstName = firstName
        self.role = role
        self.userName = userName
        self.password = password

    def get_info(self):
        return f"ID: {self.employeeID}, {self.firstName} {self.lastName}, Role: {self.role}"

    def __str__(self):
        return f"Employee[ID: {self.employeeID}, Name: {self.firstName} {self.lastName}, Role: {self.role}, Username: {self.userName}]"