import unittest

from expression_builder.expression_builder import ExpressionBuilder


class MultiStatementsTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_two_statements(self):
        result = self.exp.run_statement("result = 10;tom = 25")
        self.assertEqual(10, result['result'])
        self.assertEqual(25, result['tom'])

    def test_two_statements_second_needs_first(self):
        result = self.exp.run_statement("result = 10;tom = 25 + result")
        self.assertEqual(10, result['result'])
        self.assertEqual(35, result['tom'])

    def test_two_statements_third_needs_first(self):
        result = self.exp.run_statement("result = 10;fred=50;tom = 25 + result")
        self.assertEqual(10, result['result'])
        self.assertEqual(50, result['fred'])
        self.assertEqual(35, result['tom'])

    def test_string(self):
        result = self.exp.run_statement("result = 10;tom = 'th;omas'")
        self.assertEqual(10, result['result'])
        self.assertEqual('th;omas', result['tom'])

    def test_variable_in_second(self):
        result = self.exp.run_statement("a = 10;b = tom", variables={'tom': 100})
        self.assertEqual(10, result['a'])
        self.assertEqual(100, result['b'])
