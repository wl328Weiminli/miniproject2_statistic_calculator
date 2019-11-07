def square_root(a):
    c = a ** 0.5
    if c > 10:
        c = round(c, 8)
    else:
        c = round(c, 9)
    return c