from Statistics.z_score import z_score


def population_correlation_coefficient(num, num1):
    z1 = z_score(num)
    z2 = z_score(num1)
    z1_z2 = list(map(lambda x, y: x * y, z1, z2))
    p = sum(z1_z2) / len(z1_z2)
    return p