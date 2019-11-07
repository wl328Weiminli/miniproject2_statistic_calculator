from Statistics.proportion import proportion
from Statistics.population_variance import population_variance


def variance_of_population_proportion(num):
    variance_p = proportion(num)
    return population_variance(variance_p)