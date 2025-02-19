class Shape:
    def __init__(self, color):
        self.color = color

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def get_information(self):
        return f"{self.color}"

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return (self.length + self.width) * 2.0

    def get_information(self):
        return super().get_information() + (f"\nRectangle\nLength: {self.length}\nWidth: {self.width}\n"
                                            f"Area: {self.calculate_area()}\n"
                                            f"Perimeter: {self.calculate_perimeter()}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * 3.14

    def calculate_perimeter(self):
        return (self.radius * 2) * 3.14

    def get_information(self):
        return super().get_information() + (f"\nCircle\nRadius: {self.radius}\n"
                                            f"Area: {self.calculate_area()}\n"
                                            f"Perimeter: {self.calculate_perimeter()}")

class Square(Rectangle):
    def __init__(self, color, width):
        super().__init__(color, width, width)

    def calculate_area(self):
        return self.width * self.width

    def calculate_perimeter(self):
        return self.width * 4.0

    def get_information(self):
        return (f"Square\nLength: {self.length}\nWidth: {self.width}\n"
                                            f"Area: {self.calculate_area()}\n"
                                            f"Perimeter: {self.calculate_perimeter()}")

class TestShape:
    def __init__(self):
        self.rectangle = Rectangle("Red", 4, 3)
        self.circle = Circle("Yellow", 3)
        self.square = Square("Blue", 6)

    def display_info(self):
        print(self.rectangle.get_information())
        print("------------------------------")
        print(self.circle.get_information())
        print("------------------------------")
        print(self.square.get_information())

res = TestShape()
res.display_info()