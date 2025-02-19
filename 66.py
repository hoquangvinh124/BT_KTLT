from datetime import *

class Mammal:
    def set_date_of_birth(self):
        pass

    def get_age_as_days(self):
        pass

class BloodGroup:
    def __init__(self, blood_group):
        self._blood_group = blood_group

    def get_blood_group(self):
        return self._blood_group

class Address:
    def __init__(self, post_code):
        self._post_code = post_code

    def get_post_code(self):
        return self._post_code


class Person(Mammal):
    def __init__(self, first_name, blood_group, dob):
        self.first_name = first_name
        self.blood_group = BloodGroup(blood_group)
        self.addresses = []
        self.dob = dob

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_age_as_days(self):
        if self.dob:
            return (date.today() - self.dob).days

    def set_dob(self, dob):
        self.dob = dob

    def add_address(self, postcode):
        self.addresses.append(Address(postcode))

    def get_addresses(self):
        return [address.get_post_code() for address in self.addresses]

    def __str__(self):
        return f"Name: {self.first_name}, Blood Group: {self.blood_group.get_blood_group()}, Age (days): {self.get_age_as_days()}"


class Man(Person):
    def __init__(self, first_name, blood_group, dob):
        super().__init__(first_name, blood_group, dob)
        self.watching_football = False

    def __str__(self):
        return super().__str__() + f", Watching Football: {self.is_watching_football()}"

    def watch_football(self):
        self.watching_football = True

    def is_watching_football(self):
        return self.watching_football


class Woman(Person):
    def __init__(self, first_name, blood_group, dob):
        super().__init__(first_name, blood_group, dob)
        self.wearing_makeup = False

    def put_makeup_on(self):
        self.wearing_makeup = True

    def is_wearing_makeup(self):
        return self.wearing_makeup

    def __str__(self):
        return super().__str__() + f", Wearing Makeup: {self.is_wearing_makeup()}"



man = Man("Vinh", "O", dob=date(2005,12,11))
man.add_address("87925")
man.watch_football()

print(man)
print("Addresses:", man.get_addresses())


woman = Woman("Tlinh", "A", dob=date(2000,10,7))
woman.put_makeup_on()
woman.add_address("67890")

print(woman)
print("Addresses:", woman.get_addresses())