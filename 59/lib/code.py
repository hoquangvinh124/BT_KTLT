class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
    def get_numerator(self):
        return self.__numerator
    def set_denominator(self, denominator):
        self.__denominator = denominator
    def get_denominator(self):
        return self.__denominator
    def set_numerator(self, numerator):
        self.__numerator = numerator

    numerator = property(get_numerator, set_numerator, "numerator")
    denominator = property(get_denominator, set_denominator, "denominator")

    def add(self, other):
        tu=self.numerator
