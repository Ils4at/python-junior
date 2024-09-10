from block_1.common import MyException


class Value:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __mul__(self, other):
        return self.number * other

    def __truediv__(self, other):
        try:
            return self.number / other
        except ZeroDivisionError:
            raise MyException(Exception)

    # def __truediv__(self, other):
    #     if other != 0:
    #         return self.number / other
    #     else:
    #         raise MyException(Exception)
