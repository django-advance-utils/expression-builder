import unittest

from expression_builder.expression_builder import ExpressionBuilder


class BracketsTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_one(self):
        result = self.exp.run_statement("(2 + 4) * 2")
        self.assertEqual(12, result)

    def test_multi(self):
        result = self.exp.run_statement("(2 + 4) * (70 - 6)")
        self.assertEqual(384, result)

    def test_complex(self):
        result = self.exp.run_statement("((2 + 4) * (10 - 7)) * (70 - 6)")
        self.assertEqual(1152, result)

    def test_string(self):
        result = self.exp.run_statement("('hello')")
        self.assertEqual('hello', result)

    def test_string_closing(self):
        result = self.exp.run_statement("('h)ello')")
        self.assertEqual('h)ello', result)

    def test_string_opening(self):
        result = self.exp.run_statement("('h(ello')")
        self.assertEqual('h(ello', result)

    def test_multi_string(self):
        result = self.exp.run_statement("4*4+4*4+4-4*4")
        self.assertEqual(20, result)

    def test_bodmas_plus_minus(self):
        result = self.exp.run_statement("10-3+2")
        self.assertEqual(9, result)

    def test_bodmas_plus_minus_times(self):
        result = self.exp.run_statement("10-3+2*2")
        self.assertEqual(11, result)