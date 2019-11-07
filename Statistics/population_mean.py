from Calculator.Addition import addition


def population_mean(num):
    n_sum = addition(num)
    return n_sum / len(num)