class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __str__(self):
        return f"{self.id}\t{self.name}"