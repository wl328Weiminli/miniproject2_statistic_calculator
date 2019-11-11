import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_data = CsvReader('Tests/Data/Test_Data.csv').data
    column = [int(row['data1']) for row in test_data]
    column1 = [int(row['data2']) for row in test_data]
    test_answer = CsvReader("Tests/Data/Test_dataAnswer.csv").data
    proportion_answer = CsvReader("Tests/Data/Test_proportionAnswer.csv").data
    z_scoreAnswer = CsvReader("Tests/Data/Test_zScoreAnswer.csv").data
    answer_column = [float(row['proportion']) for row in proportion_answer]
    answer_column1 = [float(row['z_score']) for row in z_scoreAnswer]
    sample_data = CsvReader('Tests/Data/Test_sample_data.csv').data
    sample_column = [int(row['sampleData']) for row in sample_data]

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["average"])
        self.assertEqual(self.statistics.population_mean(self.column), float(row['average']))
        self.assertEqual(self.statistics.result, float(row['average']))

    def test_median_statistics(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column), float(row['median']))
        self.assertEqual(self.statistics.result, float(row['median']))

    def test_mode_statistics(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column), [float(row['mode'])])
        self.assertEqual(self.statistics.result, [float(row['mode'])])

    def test_deviation_statistics(self):
        for row in self.test_answer:
            pprint(row["deviation"])
        self.assertEqual(self.statistics.population_standard_deviation(self.column), float(row['deviation']))
        self.assertEqual(self.statistics.result, float(row['deviation']))

    def test_variance_statistics(self):
        for row in self.test_answer:
            pprint(row["variance"])
        self.assertEqual(self.statistics.population_variance(self.column), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))

    def test_proportion_statistics(self):
        self.assertEqual(self.statistics.proportion(self.column), self.answer_column)
        self.assertEqual(self.statistics.result, self.answer_column)

    def test_variance_of_population_proportion_statistics(self):
        for row in self.test_answer:
            pprint(row["proportionVariance"])
        self.assertEqual(self.statistics.variance_of_population_proportion(self.column), float(row['proportionVariance']))
        self.assertEqual(self.statistics.result, float(row['proportionVariance']))

    def test_z_score_statistics(self):
        self.assertEqual(self.statistics.z_score(self.column), self.answer_column1)
        self.assertEqual(self.statistics.result, self.answer_column1)

    def test_population_correlation_coefficient_statistics(self):
        pprint(self.statistics.population_correlation_coefficient(self.column, self.column1))
        for row in self.test_answer:
            pprint(row["proportionVariance"])
        self.assertEqual(self.statistics.population_correlation_coefficient(self.column, self.column1),
                         float(row['population_correlation_coefficient_statistics']))
        self.assertEqual(self.statistics.result, float(row['population_correlation_coefficient_statistics']))

    def test_confidence_interval_statistics(self):
        pprint(self.statistics.confidence_interval(self.column))
        for row in self.test_answer:
            interval_element = row["confidence_interval"].split(",", 1)
            interval_result = []
            for iE in interval_element:
                fl = float(iE)
                interval_result.append(fl)
        self.assertEqual(self.statistics.confidence_interval(self.column), interval_result)
        self.assertEqual(self.statistics.result, interval_result)

    def test_sample_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["sample_mean"])
        self.assertEqual(self.statistics.sample_mean(self.sample_column), float(row['sample_mean']))
        self.assertEqual(self.statistics.result, float(row['sample_mean']))

    def test_sample_standard_deviation(self):
        for row in self.test_answer:
            pprint(row['sample_standard_deviation'])
        self.assertEqual(self.statistics.Sample_Standard_Deviation(self.sample_column),
                         float(row['sample_standard_deviation']))
        self.assertEqual(self.statistics.result, float(row['sample_standard_deviation']))

    def test_sample_variance_proportion(self):
        for row in self.test_answer:
            pprint(row['sample_variance_proportion'])
        self.assertEqual(self.statistics.sample_variance_proportion(self.sample_column),
                         float(row['sample_variance_proportion']))
        self.assertEqual(self.statistics.result, float(row['sample_variance_proportion']))


if __name__ == '__main__':
    unittest.main()
