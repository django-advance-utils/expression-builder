import unittest

from expression_builder.expression_builder import ExpressionBuilder


class GlobalTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.data = {'fred': 123, 'tom': 234}
        self.data2 = {'bill': '123-23', 'will': '234+bill'}

    def test_global_dict(self):
        exp = ExpressionBuilder()
        exp.add_to_global_dict(self.data)
        result = exp.run_statement("tom")
        self.assertEqual(234, result)

    def test_global_dict2(self):
        exp = ExpressionBuilder()
        exp.add_to_global_dict(self.data)
        result = exp.run_statement("fred")
        self.assertEqual(123, result)

    def test_global_statement_dict(self):
        exp = ExpressionBuilder()
        exp.add_to_global_statement_dict(self.data2)
        result = exp.run_statement("bill")
        self.assertEqual(100, result)

    def test_global_statement_dict2(self):
        exp = ExpressionBuilder()
        exp.add_to_global_statement_dict(self.data2)
        result = exp.run_statement("will")
        self.assertEqual(334, result)
