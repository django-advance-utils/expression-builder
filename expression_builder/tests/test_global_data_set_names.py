import unittest

from expression_builder.expression_builder import ExpressionBuilder


class GlobalDataSetNameTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_to_global("fred", 1234, inheritance_level=1, set_name='main')
        self.exp.add_to_global("fred2", 1235, inheritance_level=1, set_name='main')
        self.exp.add_to_global_statement("tom", "1+4", set_name='main')

    def test_global_variable(self):
        result = self.exp.run_statement("result = fred")
        self.assertEqual(1234, result['result'])

    def test_global_statement(self):
        result = self.exp.run_statement("result = tom")
        self.assertEqual(5, result['result'])
