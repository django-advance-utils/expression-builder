import unittest

from expression_builder.expression_builder import ExpressionBuilder


class SimpleTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_single_number(self):
        result = self.exp.run_statement("4")
        self.assertEqual(4, result)

    def test_single_negative_number(self):
        result = self.exp.run_statement("-4")
        self.assertEqual(-4, result)

    def test_add(self):
        result = self.exp.run_statement("4 + 10")
        self.assertEqual(14, result)

    def test_add_no_spaces(self):
        result = self.exp.run_statement("4+10")
        self.assertEqual(14, result)

    def test_times(self):
        result = self.exp.run_statement("4 * 10")
        self.assertEqual(40, result)

    def test_minus(self):
        result = self.exp.run_statement("10 - 4")
        self.assertEqual(6, result)

    def test_divide(self):
        result = self.exp.run_statement("10 / 2")
        self.assertEqual(5, result)

    def test_decimal(self):
        result = self.exp.run_statement("10.5")
        self.assertEqual(10.5, result)

    def test_decimal2(self):
        result = self.exp.run_statement("10.5 - 1.5")
        self.assertEqual(9, result)

    def test_multi_add(self):
        result = self.exp.run_statement("10 + 5 + 20")
        self.assertEqual(35, result)

    def test_multi_op(self):
        result = self.exp.run_statement("10 + 5 - 6")
        self.assertEqual(9, result)

    def test_multi_op2(self):
        result = self.exp.run_statement("2 + 4 * 2")
        self.assertEqual(10, result)

    def test_multi_op3(self):
        result = self.exp.run_statement("2 + 4 * 2 * 7")
        self.assertEqual(58, result)

    def test_silly(self):
        result = self.exp.run_statement("10 + -7")
        self.assertEqual(3, result)

    def test_string(self):
        result = self.exp.run_statement("'tom'")
        self.assertEqual('tom', result)

    def test_string2(self):
        result = self.exp.run_statement("'t()m'")
        self.assertEqual('t()m', result)

    def test_int_type(self):
        result = self.exp.run_statement(3)
        self.assertEqual(3, result)

    def test_float_type(self):
        result = self.exp.run_statement(3.5)
        self.assertEqual(3.5, result)

    def test_boolean_type_true(self):
        result = self.exp.run_statement(True)
        self.assertEqual(True, result)

    def test_boolean_type_false(self):
        result = self.exp.run_statement(False)
        self.assertEqual(False, result)

    def test_minus_at_start_1(self):
        result = self.exp.run_statement("-3 + 4")
        self.assertEqual(1, result)

    def test_1234(self):
        result = self.exp.run_statement("3 + 4")
        self.assertEqual(7, result)

    def test_minus2(self):
        result = self.exp.run_statement("-(3 + 4)")
        self.assertEqual(-7, result)

    def test_minus3(self):
        result = self.exp.run_statement("3 + -4")
        self.assertEqual(-1, result)

    def test_minus4(self):
        result = self.exp.run_statement("10 + (-8 + 4)")
        self.assertEqual(6, result)

    def test_minus5(self):
        result = self.exp.run_statement("-8 + 4")
        self.assertEqual(-4, result)
