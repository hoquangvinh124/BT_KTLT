from math import gcd
class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()
    def get_numerator(self):
        return self.__numerator
    def set_denominator(self, denominator):
        self.__denominator = denominator
    def get_denominator(self):
        return self.__denominator
    def set_numerator(self, numerator):
        self.__numerator = numerator
    def reduce(self):
        common_divisor = gcd(self.__numerator, self.__denominator)
        self.__numerator //= common_divisor
        self.__denominator //= common_divisor

        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    numerator = property(get_numerator, set_numerator, "numerator")
    denominator = property(get_denominator, set_denominator, "denominator")

    def add(self, other):
        new_numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.__numerator * other.numerator
        new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        new_numerator = self.__numerator * other.denominator
        new_denominator = self.__denominator * other.numerator
        return Fraction(new_numerator, new_denominator)




