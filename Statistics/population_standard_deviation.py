from Calculator.SquareRoot import square_root
from Statistics.population_mean import population_mean


def population_standard_deviation(num):
    average = population_mean(num)
    s = 0.0
    for i in num:
        s += (i - average) ** 2
    return square_root(float(s) / len(num))