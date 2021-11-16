import unittest

from expression_builder.expression_builder import ExpressionBuilder


class StatementTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_statement_variable(self):
        result = self.exp.run_statement("result = tom", statement_variables={'tom': '1+4'})
        self.assertEqual(5, result['result'])

