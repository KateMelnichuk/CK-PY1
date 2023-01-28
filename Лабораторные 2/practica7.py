class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)


    def is_leap_year(self):
        """Проверяет, является ли год високосным"""
        if self.year % 4 == 0:
            return True
        else:
            return False

    def get_max_day(self):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year():
            return self.DAY_OF_MONTH[1][self.month-1]
        else:
            return self.DAY_OF_MONTH[0][self.month-1]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not 0 < day <= 31:
            raise ValueError("day cannot be more than 31")
        if not 0 < month <= 12:
            raise ValueError("month cannot be more than 12")
        if year <= 0:
            raise ValueError("year cannot be less than 0")


date1 = Date(4,5,1998)
print(date1.is_leap_year())
print(date1.get_max_day())