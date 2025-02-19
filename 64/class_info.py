from datetime import datetime

class Employee:
    def __init__(self, id, name, id_card, birthday):
        self.id = id
        self.name = name
        self.id_card = id_card
        self.birthday = datetime.strptime(birthday, "%d-%m-%Y")

    def calculate_salary(self):
        pass

    def display_info(self):
        return f"{self.id} - {self.name} - {self.birthday.strftime('%Y')}"


class TemporaryEmployee(Employee):
    working_salary = 30000
    def __init__(self, birthday, id, id_card, name, working_day):
        super().__init__(birthday, id, id_card, name)
        self.working_day = working_day

    def calculate_salary(self):
        return self.working_day * self.working_salary

class OfficialEmployee(Employee):
    working_salary = 20000000
    def __init__(self, birthday, id, id_card, name):
        super().__init__(birthday, id, id_card, name)

    def calculate_salary(self):
        return self.working_salary

class ListOfEmployee:
    def __init__(self):
        self.arr = []

    def add_employee(self, employee):
        self.arr.append(employee)

    def filter_by_dob(self, year):
        return [emp for emp in self.arr if emp.birthday.strftime('%Y') == str(year)]

    def remove_employee(self, code):
        success = False
        for i,employee in enumerate(self.arr):
            if employee.id == code:
                self.arr.pop(i)
                success = True
        if not success:
            print("Code not found to delete")
        return self.arr

    def search_id_card(self, id_card):
        filtered_employee = [employee for employee in self.arr if id_card in employee.id_card]
        return filtered_employee




