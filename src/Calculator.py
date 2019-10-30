def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    c = b / a
    c = round(c, 9)
    return c


def square(a):
    a = int(a)
    c = a ** 2
    return c


def square_root(a):
    a = int(a)
    c = a ** 0.5
    if c > 10:
        c = round(c, 8)
    else:
        c = round(c, 9)

    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
