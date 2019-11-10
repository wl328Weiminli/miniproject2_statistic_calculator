from Calculator.Addition import addition


def proportion(num):
    proportion_list = []
    for g in num:
        h = g / addition(num)
        proportion_list.append(h)
    return proportion_list
