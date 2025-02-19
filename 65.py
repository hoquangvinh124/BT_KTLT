
class StaffMember:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def pay(self):
        pass

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}"

class Volunteer(StaffMember):
    def __init__(self, name, address, phone):
        super().__init__(name, address, phone)

    def pay(self):
        return 100.0

    def __str__(self):
        return "Volunteer:\n" + super().__str__()


class Employee(StaffMember):
    def __init__(self, name, address, phone, social_security_number, pay_rate=3000):
        super().__init__(name, address, phone)
        self.social_security_number = social_security_number
        self.pay_rate = pay_rate

    def pay(self):
        return self.pay_rate

    def __str__(self):
        return (f"Employee:\n{super().__str__()}\nSocial Security Number: {self.social_security_number}\n"
                f"Pay Rate: {self.pay_rate}")


class Executive(Employee):
    def __init__(self, name, address, phone, social_security_number, pay_rate=3000):
        super().__init__(name, address, phone, social_security_number, pay_rate)
        self.bonus = 0.0

    def award_bonus(self, bonus):
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus

    def __str__(self):
        return "Executive:\n" + super().__str__() + f"\nBonus: {self.bonus}"


class Hourly(Employee):
    def __init__(self, name, address, phone, social_security_number, pay_rate=0):
        super().__init__(name, address, phone, social_security_number, pay_rate)
        self.hours_worked = 0

    def add_hours(self, hours):
        self.hours_worked += hours

    def pay(self):
        return 10.0 * self.hours_worked

    def __str__(self):
        return "Hourly:\n" + super().__str__() + f"\nHours Worked: {self.hours_worked}"


class Staff:
    def __init__(self):
        self.staff_list = [
            Volunteer("Vinh", "Quy Nhon", "0919691057"),
            Employee("Tlinh", "Sai Gon", "0987654321", "1455454"),
            Executive("Phuc Du", "Ha Noi", "0111111111", "5965565"),
            Hourly("Mck", "Sai Gon", "0222222222", "5456565"),
            Volunteer("Wrxdie", "Da Nang", "0333333333")
        ]

        exec_member = self.staff_list[2]
        if isinstance(exec_member, Executive):
            exec_member.award_bonus(500)

        hourly_member = self.staff_list[3]
        if isinstance(hourly_member, Hourly):
            hourly_member.add_hours(20)

    def payday(self):
        for e in self.staff_list:
            print(e)
            print("Pay:", e.pay())
            print("---------------------------------")


staff = Staff()
staff.payday()
