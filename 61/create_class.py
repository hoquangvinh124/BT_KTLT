class Student:
    def __init__(self, first_name, last_name, home_address, school_address):
        self._first_name = first_name
        self._last_name = last_name
        self._home_address = home_address
        self._school_address = school_address

    def __str__(self):
        return (f"Student Name: {self._first_name} {self._last_name}\n"
                f"Home Address: {self._home_address}\n"
                f"School Address: {self._school_address}")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def home_address(self):
        return self._home_address

    @home_address.setter
    def home_address(self, home_address):
        self._home_address = home_address

    @property
    def school_address(self):
        return self._school_address

    @school_address.setter
    def school_address(self, school_address):
        self._school_address = school_address

class Address:
    def __init__(self, street_address, city, state, zip_code):
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code

    def __str__(self):
        return f"{self._street_address}, {self._city}, {self._state}, {self._zip_code}"

    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code


