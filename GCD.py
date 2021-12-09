import math


class Rational:
    """Class for creating right fractions
    Operators:
    __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __ne__, __bool__
    __add__, __sub__, __mul__, __truediv__
    Methods:
    _cmp(), float_point_format()
    """
    def __init__(self, numerator, denominator=1):
        """Constructor
        :param numerator
        :param denominator, by default 1
        :raise  ValueError, ZeroDivisionError
        """
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Type Error")
        if denominator == 0:
            raise ZeroDivisionError(f'Rational({numerator}, 0)')
        self._numerator = numerator
        self._denominator = denominator
        g = math.gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, num):
        self._numerator = num

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, num):
        self._denominator = num

    def __add__(a, b):
        """ a + b """
        return Rational(a._numerator * b._denominator + a._denominator * b._numerator, a._denominator * b._denominator)

    def __sub__(a, b):
        """ a - b """
        return Rational(a._numerator * b._denominator - a._denominator * b._numerator, a._denominator * b._denominator)

    def __mul__(a, b):
        """ a * b """
        return Rational(a._numerator * b._numerator, a._denominator * b._denominator)

    def __truediv__(a, b):
        """ a / b"""
        return Rational(a._numerator * b._denominator, b._numerator * a._denominator)

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator, self.denominator = self.numerator + other * self.denominator, self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return self

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator, self.denominator = self.numerator - other * self.denominator, self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return self

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator, self.denominator = self.numerator * other.numerator, self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator = self.numerator * other
            self.denominator = self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return self

    def __idiv__(self, other):
        if isinstance(other, Rational):
            self.numerator, self.denominator = self.numerator * other.denominator, self.denominator * other.numerator
        elif isinstance(other, int):
            self.numerator = self.numerator * other
            self.denominator = self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return self

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator == other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator != other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator != other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator > other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")
    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def float_point_format(self):
        return f'{round(self._numerator / self._denominator, 2)}'


fraction_1 = Rational(8, 10)
fraction_2 = Rational(4, 12)
fraction_3 = Rational(1, 3)
fraction_4 = Rational(0, 1)
fraction_5 = Rational(4)

print(
    fraction_1,
    fraction_2,
    fraction_5
)

print(
    fraction_1 + fraction_2,
    fraction_1 - fraction_2,
    fraction_1 * fraction_2,
    fraction_1 / fraction_2
)

print(
    fraction_1,
    fraction_1.float_point_format()
)

print(
    fraction_1 < fraction_2,
    fraction_1 > fraction_2,
    fraction_1 == fraction_2,
    fraction_1 != fraction_2,
    fraction_2 == fraction_3
)