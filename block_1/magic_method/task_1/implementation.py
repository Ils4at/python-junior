class Multiplier:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Multiplier(self.num + other.num)

    def __sub__(self, other):
        return Multiplier(self.num - other.num)

    def __mul__(self, other):
        return Multiplier(self.num * other.num)

    def __truediv__(self, other):
        return Multiplier(self.num / other.num)

    def get_value(self):
        return self.num


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, num):
        self.num = num * 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, num):
        self.num = num * 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, num):
        self.num = num * 1000000

