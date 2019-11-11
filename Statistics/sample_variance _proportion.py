from Statistics.population_variance import population_variance
from Statistics.sample_method import sample_method
from Statistics.proportion import proportion


def sample_variance_proportion(num):
    sample_list = sample_method(num)
    data_proportion = proportion(sample_list)
    return population_variance(data_proportion)





