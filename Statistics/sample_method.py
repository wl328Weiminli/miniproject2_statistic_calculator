import random


def sample_method(num):
    r = random.randint(30, 51)
    sample_list = random.sample(num, r)
    return sample_list