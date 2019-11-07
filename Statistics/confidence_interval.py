from Statistics.population_mean import population_mean
from Statistics.population_standard_deviation import population_standard_deviation
from Calculator.SquareRoot import square_root


def confidence_interval(num):
    x1 = population_mean(num)
    c = 0.95
    z_value = (1-c) / 2
    d1 = population_standard_deviation(num)
    l1 = square_root(len(num))
    return [x1 - z_value*d1 / l1, x1 + z_value*d1 / l1]