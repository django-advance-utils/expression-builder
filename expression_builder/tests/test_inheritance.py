import unittest

from expression_builder.expression_builder import ExpressionBuilder


class InheritanceTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_to_global("fred", 1234, inheritance_level=1)
        self.exp.add_to_global("william100", 55, inheritance_level=2)
        self.exp.add_to_global("i1t", 2)

    def test_inheritance_level(self):
        self.exp.run_statement("fred + william100")
        self.assertEqual(2, self.exp.get_inheritance_level())
        self.exp.reset_highest_inheritance_level()
        self.assertEqual(-1, self.exp.get_inheritance_level())

    def test_inheritance_level_2(self):
        self.exp.run_statement("i1t")
        self.assertEqual(-1, self.exp.get_inheritance_level())

    def test_inheritance_level_3(self):
        self.exp.run_statement("i1t", statement_inheritance_level=3)
        self.assertEqual(3, self.exp.get_inheritance_level())

    def test_inheritance_level_4(self):
        self.exp.run_statement("fred + william100", statement_inheritance_level=3)
        self.assertEqual(3, self.exp.get_inheritance_level())
