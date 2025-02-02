import json

class Employee:
    def __init__(self,full_name,gender,city):
        self.fullName = full_name
        self.gender = gender
        self.city = city

    def __str__(self):
        return json.dumps(self.__dict__)