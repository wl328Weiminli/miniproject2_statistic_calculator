import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_data = CsvReader('Tests/Data/Test_Data.csv').data
    column = [int(row['data1']) for row in test_data]
    column2 = [int(row['data2']) for row in test_data]
    test_answer = CsvReader("Tests/Data/Test_dataAnswer.csv").data
    pprint(column)

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        for row in self.test_answer:
            pprint(row["average"])
        self.assertEqual(self.statistics.population_mean(self.column), float(row['average']))
        self.assertEqual(self.statistics.result, float(row['average']))

    def test_median_statistic(self):
        for row in self.test_answer:
            pprint(row["median"])
        self.assertEqual(self.statistics.median(self.column), float(row['median']))
        self.assertEqual(self.statistics.result, float(row['median']))

    def test_mode_statistic(self):
        for row in self.test_answer:
            pprint(row["mode"])
        self.assertEqual(self.statistics.mode(self.column), [float(row['mode'])])
        self.assertEqual(self.statistics.result, [float(row['mode'])])

    def test_deviation_statistic(self):
        for row in self.test_answer:
            pprint(row["deviation"])
        self.assertEqual(self.statistics.population_standard_deviation(self.column), float(row['deviation']))
        self.assertEqual(self.statistics.result, float(row['deviation']))

    def test_variance_statistic(self):
        for row in self.test_answer:
            pprint(row["variance"])
        self.assertEqual(self.statistics.population_variance(self.column), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))

    def test_proportion_statistic(self):
        proportion_answer = CsvReader("Tests/Data/Test_proportionAnswer.csv").data
        answer_column = [float(row['proportion']) for row in proportion_answer]
        self.assertEqual(self.statistics.proportion(self.column), answer_column)
        self.assertEqual(self.statistics.result, answer_column)




if __name__ == '__main__':
    unittest.main()
