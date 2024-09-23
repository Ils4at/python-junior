from datetime import time


def count_m(h, m):
    if m >= 60 or m < 0:
        i = m // 60
        h += i
        if h > 24 or h < 0:
            h %= 24
        m %= 60
    return h, m


class MathClock:
    def __init__(self):
        self.oclock = time(hour=00, minute=00)

    def __add__(self, other):
        h = self.oclock.hour
        m = self.oclock.minute
        m += other
        h, m = count_m(h, m)
        self.oclock = time(hour=h, minute=m)

    def __sub__(self, other):
        h = self.oclock.hour
        m = self.oclock.minute
        m -= other
        h, m = count_m(h, m)
        self.oclock = time(hour=h, minute=m)

    def __mul__(self, other):
        h = self.oclock.hour
        m = self.oclock.minute
        h += other
        if h >= 24:
            h %= 24
        self.oclock = time(hour=h, minute=m)

    def __truediv__(self, other):
        h = self.oclock.hour
        m = self.oclock.minute
        h -= other
        if h < 0:
            h %= 24
        self.oclock = time(hour=h, minute=m)

    def get_time(self):
        return self.oclock.strftime('%H:%M')
