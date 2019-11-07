from Statistics.population_standard_deviation import population_standard_deviation
from Calculator.Square import square


def population_variance(num):
    deviation = population_standard_deviation(num)
    return square(deviation)