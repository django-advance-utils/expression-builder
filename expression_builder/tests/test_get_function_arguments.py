import unittest

from expression_builder.expression_builder import ExpressionBuilder


class GetFunctionArgumentsTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_one_arg(self):
        result = self.exp.get_function_arguments('abc')
        expected_results = ['abc']
        self.assertEqual(expected_results, result)

    def test_two_arg(self):
        result = self.exp.get_function_arguments('abc,cdf')
        expected_results = ['abc', 'cdf']
        self.assertEqual(expected_results, result)

    def test_two_arg_brackets(self):
        result = self.exp.get_function_arguments('abc,(c,df)')
        expected_results = ['abc', '(c,df)']
        self.assertEqual(expected_results, result)

    def test_two_arg_quotes(self):
        result = self.exp.get_function_arguments('a"b,c"d,test')
        expected_results = ['a"b,c"d', 'test']
        self.assertEqual(expected_results, result)
