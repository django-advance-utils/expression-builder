import unittest

from expression_builder.expression_builder import ExpressionBuilder


class VariableUsedTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_to_global("fred", 1234)

    def test_global_single(self):
        self.exp.run_statement("result = fred")
        self.assertEqual({'fred': 1}, self.exp.get_used_variables())

    def test_global_double(self):
        self.exp.run_statement("result = fred+fred")
        self.assertEqual({'fred': 2}, self.exp.get_used_variables())

    def test_local_single(self):
        self.exp.run_statement("result = tom", variables={'tom': 5})
        self.assertEqual({'tom': 1}, self.exp.get_used_variables())

    def test_local_double(self):
        self.exp.run_statement("result = tom+tom", variables={'tom': 5})
        self.assertEqual({'tom': 2}, self.exp.get_used_variables())

    def test_mix(self):
        self.exp.run_statement("result = tom+fred", variables={'tom': 5})
        self.assertEqual({'tom': 1, 'fred': 1}, self.exp.get_used_variables())

