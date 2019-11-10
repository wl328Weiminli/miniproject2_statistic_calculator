from Statistics.sample_method import sample_method
from Statistics.population_mean import population_mean


def sample_mean(num):
    sample_list1 = sample_method(num)
    return population_mean(sample_list1)
