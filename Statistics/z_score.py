from Statistics.population_mean import population_mean
from Statistics.population_standard_deviation import population_standard_deviation


def z_score(num):
    average1 = population_mean(num)
    deviation1 = population_standard_deviation(num)
    score_list = []
    for x in num:
        f = (x - average1) / deviation1
        score_list.append(f)
    return score_list
