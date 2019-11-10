import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


# from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('Tests/Data/Test_Addition.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.addition([int(row['Value 1']), int(row['Value 2'])]), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('Tests/Data/Test_Subtraction.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtraction(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('Tests/Data/Test_Multiplication.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiplication(int(row['Value 1']), int(row['Value 2'])),
                             int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('Tests/Data/Test_Division.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.division(int(row['Value 1']), int(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_Square(self):
        test_data = CsvReader('Tests/Data/Test_Square.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_SquareRoot(self):
        test_data = CsvReader('Tests/Data/Test_SquareRoot.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.square_root(int(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
