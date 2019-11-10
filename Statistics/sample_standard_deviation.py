from Statistics.sample_mean import sample_mean
from Statistics.population_standard_deviation import population_standard_deviation


def Sample_Standard_Deviation(num):
    sample_average = sample_mean(num)
    return population_standard_deviation(sample_average)
