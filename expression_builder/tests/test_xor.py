import unittest

from expression_builder.expression_builder import ExpressionBuilder


class XORTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_xor_no_no(self):
        result = self.exp.run_statement("no XOR no;")
        self.assertEqual(False, result)

    def test_xor_no_yes(self):
        result = self.exp.run_statement("no XOR yes;")
        self.assertEqual(True, result)

    def test_xor_yes_no(self):
        result = self.exp.run_statement("yes XOR no;")
        self.assertEqual(True, result)

    def test_xor_yes_yes(self):
        result = self.exp.run_statement("yes XOR yes;")
        self.assertEqual(False, result)

    def test_var(self):
        result = self.exp.run_statement("j_curtail_required =='yes' XOR j_bullnose_required =='yes'",
                                        variables={'j_curtail_required': 'no',
                                                   'j_bullnose_required': 'yes'})
        self.assertEqual(True, result)