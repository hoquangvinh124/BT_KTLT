class Employee:
    def __init__(self, employee_id, employee_name, username, password):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.employee_id}\t{self.employee_name}"
