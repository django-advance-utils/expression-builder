import unittest

from expression_builder.expression_builder import ExpressionBuilder


class LogicTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_true(self):
        result = self.exp.run_statement("true;")
        self.assertEqual(True, result)

    def test_false(self):
        result = self.exp.run_statement("result = false;")
        self.assertEqual(False, result['result'])

    def test_true_camelcase(self):
        result = self.exp.run_statement("True")
        self.assertEqual(True, result)

    def test_false_camelcase(self):
        result = self.exp.run_statement("False")
        self.assertEqual(False, result)

    def test_yes(self):
        result = self.exp.run_statement("result = yes;")
        self.assertEqual(True, result['result'])

    def test_no(self):
        result = self.exp.run_statement("result = no;")
        self.assertEqual(False, result['result'])

    def test_yes_2(self):
        result = self.exp.run_statement("yes")
        self.assertEqual(True, result)

    def test_no_2(self):
        result = self.exp.run_statement("no")
        self.assertEqual(False, result)

    def test_yes_camelcase(self):
        result = self.exp.run_statement("Yes")
        self.assertEqual(True, result)

    def test_no_camelcase(self):
        result = self.exp.run_statement("No")
        self.assertEqual(False, result)

    def test_default_assignment(self):
        result = self.exp.run_statement("result = 17;")
        self.assertEqual(17, result['result'])

    def test_default_string_assignment(self):
        result = self.exp.run_statement("result = 'tom';")
        self.assertEqual('tom', result['result'])

    def test_default_string2_assignment(self):
        result = self.exp.run_statement("result = 'Thomas Turner';")
        self.assertEqual('Thomas Turner', result['result'])

    def test_default_string3_assignment(self):
        result = self.exp.run_statement('result = "Thomas Turner";')
        self.assertEqual('Thomas Turner', result['result'])

    def test_default_string4_assignment(self):
        result = self.exp.run_statement("result = 'Tom\\'s';")
        self.assertEqual('Tom\'s', result['result'])

    def test_default_string5_assignment(self):
        result = self.exp.run_statement('result = "Tom\\"s";')
        self.assertEqual('Tom"s', result['result'])

    def test_default_string6_assignment(self):
        result = self.exp.run_statement('result = "Tom\'s";')
        self.assertEqual('Tom\'s', result['result'])

    def test_assignment_eq_t(self):
        result = self.exp.run_statement("result = 17==17;")
        self.assertEqual(True, result['result'])

    def test_assignment_eq_f(self):
        result = self.exp.run_statement("result = 17 == 1;")
        self.assertEqual(False, result['result'])

    def test_assignment_ne_t(self):
        result = self.exp.run_statement("result = 17 != 15;")
        self.assertEqual(True, result['result'])

    def test_assignment_ne(self):
        result = self.exp.run_statement("result = 17 != 17;")
        self.assertEqual(False, result['result'])

    def test_assignment_gt_t(self):
        result = self.exp.run_statement("result = 17 > 16;")
        self.assertEqual(True, result['result'])

    def test_assignment_gt_ts(self):
        result = self.exp.run_statement("17 > 16;")
        self.assertEqual(True, result)

    def test_assignment_gt(self):
        result = self.exp.run_statement("result = 17 > 17;")
        self.assertEqual(False, result['result'])

    def test_assignment_gt2(self):
        result = self.exp.run_statement("result = 17 >= 17;")
        self.assertEqual(True, result['result'])

    def test_assignment_lt_t(self):
        result = self.exp.run_statement("result = 17 < 18;")
        self.assertEqual(True, result['result'])

    def test_assignment_lt(self):
        result = self.exp.run_statement("result = 17 < 17;")
        self.assertEqual(False, result['result'])

    def test_assignment_lt2(self):
        result = self.exp.run_statement("result = 17 <= 17;")
        self.assertEqual(True, result['result'])

    def test_true2(self):
        result = self.exp.run_statement("result = true;")
        self.assertEqual(True, result['result'])

    def test_or_false(self):
        result = self.exp.run_statement("result = false || false;")
        self.assertEqual(False, result['result'])

    def test_or_true(self):
        result = self.exp.run_statement("result = false || true;")
        self.assertEqual(True, result['result'])

    def test_and_false(self):
        result = self.exp.run_statement("result = false && false;")
        self.assertEqual(False, result['result'])

    def test_and_false2(self):
        result = self.exp.run_statement("result = true && false;")
        self.assertEqual(False, result['result'])

    def test_and_false3(self):
        result = self.exp.run_statement("result = false && true;")
        self.assertEqual(False, result['result'])

    def test_and_true(self):
        result = self.exp.run_statement("result = true && true;")
        self.assertEqual(True, result['result'])

    def test_and_true2(self):
        result = self.exp.run_statement("result = 100 > 10 && 10 == 10;")
        self.assertEqual(True, result['result'])

    def test_double_eq_true(self):
        result = self.exp.run_statement("1 == 1;")
        self.assertEqual(True, result)

    def test_double_eq_false(self):
        result = self.exp.run_statement("1 == 0;")
        self.assertEqual(False, result)

    def test_double_string_eq_true(self):
        result = self.exp.run_statement("'yes' == 'yes';")
        self.assertEqual(True, result)

    def test_double_string_eq_false(self):
        result = self.exp.run_statement("'yes' == 'no';")
        self.assertEqual(False, result)

    def test_compare_blanks_true(self):
        result = self.exp.run_statement("'' == '';")
        self.assertEqual(True, result)

    def test_compare_blanks_false(self):
        result = self.exp.run_statement("'' != '';")
        self.assertEqual(False, result)

    def test_advance(self):
        result = self.exp.run_statement("x_options == 1;", variables={'x_options': 1})
        self.assertEqual(True, result)

