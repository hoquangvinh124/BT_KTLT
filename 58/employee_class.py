class Employee:
    def __init__(self, last_name, first_name, number_of_products):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__number_of_products = number_of_products

    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_number_of_products(self):
        return self.__number_of_products
    def set_number_of_products(self, number_of_products):
        if number_of_products < 0:
            self.__number_of_products = 0
        self.__number_of_products = number_of_products
        return
    def set_last_name(self, last_name):
        self.__last_name = last_name
        return
    def set_first_name(self, first_name):
        self.__first_name = first_name
        return

    def get_salary(self):
        unit_price = 0
        if 1 >= self.__number_of_products >= 199:
            unit_price = 0.5
        if 200 >= self.__number_of_products >= 399:
            unit_price = 0.55
        if 400 >= self.__number_of_products >= 599:
            unit_price = 0.6
        if self.__number_of_products >= 600:
            unit_price = 0.65
        salary = self.__number_of_products * unit_price
        return salary



