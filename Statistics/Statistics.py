from Calculator.Calculator import Calculator
from Statistics.population_mean import population_mean
from Statistics.median import median
from Statistics.mode import mode
from Statistics.population_standard_deviation import population_standard_deviation
from Statistics.population_variance import population_variance
from Statistics.z_score import z_score
from Statistics.population_correlation_coefficient import population_correlation_coefficient
from Statistics.variance_of_population_proportion import variance_of_population_proportion
from Statistics.confidence_interval import confidence_interval
from Statistics.proportion import proportion
from Statistics.sample_method import sample_method
from Statistics.sample_mean import sample_mean
from Statistics.sample_standard_deviation import Sample_Standard_Deviation
from Statistics.sample_variance_proportion import sample_variance_proportion
from Statistics.p_value import p_value


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, data):
        self.result = population_mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def population_standard_deviation(self, data):
        self.result = population_standard_deviation(data)
        return self.result

    def population_variance(self, data):
        self.result = population_variance(data)
        return self.result

    def z_score(self, data):
        self.result = z_score(data)
        return self.result

    def population_correlation_coefficient(self, data, data1):
        self.result = population_correlation_coefficient(data, data1)
        return self.result

    def variance_of_population_proportion(self, data):
        self.result = variance_of_population_proportion(data)
        return self.result

    def confidence_interval(self, data):
        self.result = confidence_interval(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def sample_method(self, data):
        self.result = sample_method(data)
        return self.result

    def sample_mean(self, data):
        self.result = sample_mean(data)
        return self.result

    def Sample_Standard_Deviation(self, data):
        self.result = Sample_Standard_Deviation(data)
        return self.result

    def sample_variance_proportion(self, data):
        self.result = sample_variance_proportion(data)
        return self.result

    def p_value(self, data):
        self.result = p_value(data)
        return self.result
