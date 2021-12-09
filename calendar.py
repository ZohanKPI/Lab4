MAX_YEAR = 9999
MIN_YEAR = 1
class Calendar:
    def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, day_):
        if not (isinstance(day_, int) or 1 <= day_ <= 31):
            raise TypeError("Incorrect input")
        self._day = day_
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, month_):
        if not (isinstance(month_, int) or 1 <= month_ <= 12):
            raise TypeError("Incorrect input")
        self._month = month_
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year_):
        if not isinstance(year_, int) or MIN_YEAR <= year_ < MAX_YEAR:
            raise TypeError("Incorrect input")
        self._year = year_

    def leap_year(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def __add__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Needs to be a Calendar class object")
        return self.day + other.day, self.month + other.month, self.year + other.year

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Needs to be a Calendar class object")
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Needs to be a Calendar class object")
        return (self.day, self.month, self.year) > (other.day, other.month, other.year)

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Needs to be a Calendar class object")
        return (self.day, self.month, self.year) < (other.day, other.month, other.year)

    def __iadd__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Operations with Calendar only allowed")
        self.year += other.year
        return self

    def __isub__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Operations with Calendar only allowed")
        self.year -= other.year
        return self


if __name__ == "__main__":
    x = Calendar(11, 9, 2003)
    y = Calendar(10, 10, 2004)

    x += y
    print(x)

    for i in range(10):
        x -= y
        print(x)

    print(f"{x == y = }")
    print(f"{x != y = }")
    print(f"{x > y = }")
    print(f"{x < y = }")
    print(f"{x >= y = }")
    print(f"{x <= y = }")

