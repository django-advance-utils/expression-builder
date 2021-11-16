import unittest

from expression_builder.expression_builder import ExpressionBuilder


class GlobalDataTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_to_global("fred", 1234, inheritance_level=1)
        self.exp.add_to_global("william100", 55, inheritance_level=2)
        self.exp.add_to_global("i1u", 'yes')
        self.exp.add_to_global("i1w", 1)
        self.exp.add_to_global("i1t", 2)
        self.exp.add_to_global_statement("tom", "1+4")
        self.exp.add_to_global_statement("bill", "william$")
        self.exp.add_to_global_statement("qm", "'yes'=='yes'")
        self.exp.add_to_global_statement("n", None)
        self.exp.add_to_global_statement("vw", 'i$u == "Width"? i$w: i$t;')
        self.exp.add_to_global_statement("e_text", "$.v=='thickness'?'thickness':'width';")

    def test_global_variable(self):
        result = self.exp.run_statement("result = fred")
        self.assertEqual(1234, result['result'])

    def test_global_statement(self):
        result = self.exp.run_statement("result = tom")
        self.assertEqual(5, result['result'])

    def test_global_replace_statement(self):
        result = self.exp.run_statement("result = bill", replace_values={"$": "100"})
        self.assertEqual(55, result['result'])

    def test_global_question_mark(self):
        result = self.exp.run_statement("result = qm")
        self.assertEqual(True, result['result'])

    def test_global_question_mark2(self):
        result = self.exp.run_statement("vw", replace_values={"$": "1"})
        self.assertEqual(2, result)

    def test_global_none(self):
        result = self.exp.run_statement("result = n")
        self.assertEqual("", result['result'])

    def test_thickness(self):

        self.exp.add_to_global('i_test.v', 'thickness')
        result = self.exp.run_statement("e_text", replace_values={"$": "i_test"})
        self.assertEqual("thickness", result)

    def test_width(self):
        self.exp.add_to_global('i_test.v', 'width')
        result = self.exp.run_statement("e_text", replace_values={"$": "i_test"})
        self.assertEqual("width", result)
