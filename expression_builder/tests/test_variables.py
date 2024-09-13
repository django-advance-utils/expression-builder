import unittest

from expression_builder.expression_builder import ExpressionBuilder


class VariablesTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.vars = {'tom': 30, 'fred': 3, 'tommy': 66, 'noboby': None, 'blank': ''}

    def test_single(self):
        result = self.exp.run_statement("tom", variables=self.vars)
        self.assertEqual(30, result)

    def test_multi(self):
        result = self.exp.run_statement("tom + fred", variables=self.vars)
        self.assertEqual(33, result)

    def test_multi2(self):
        result = self.exp.run_statement("tommy - tom", variables=self.vars)
        self.assertEqual(36, result)

    def test_multi3(self):
        result = self.exp.run_statement("tom+tom", variables=self.vars)
        self.assertEqual(60, result)

    def test_multi_mix(self):
        result = self.exp.run_statement("tommy - 5", variables=self.vars)
        self.assertEqual(61, result)

    def test_complex(self):
        result = self.exp.run_statement("(tommy - 5) * tom", variables=self.vars)
        self.assertEqual(1830, result)

    def test_none(self):
        result = self.exp.run_statement('result = noboby;', variables=self.vars)
        self.assertEqual(None, result['result'])

    def test_blank(self):
        result = self.exp.run_statement('result = blank;', variables=self.vars)
        self.assertEqual('', result['result'])

    def test_single_answers(self):
        hang_variables = {'hang': 'left'}

        result = self.exp.run_statement("hang == 'left'", variables=hang_variables)
        self.assertEqual(True, result)

    def test_multi_answers(self):
        hang_variables = {'hang': ['left_hung', 'left']}

        result = self.exp.run_statement("hang == 'left'", variables=hang_variables)
        self.assertEqual(True, result)

    def test_multi_answer_no(self):
        hang_variables = {'hang': ['left_hung', 'left']}

        result = self.exp.run_statement("hang == 'left2'", variables=hang_variables)
        self.assertEqual(False, result)

    def test_not_in_multi_answers(self):
        hang_variables = {'hang': ['left_hung', 'left']}

        result = self.exp.run_statement("hang != 'left'", variables=hang_variables)
        self.assertEqual(False, result)

    def test_not_in_multi_answers_no(self):
        hang_variables = {'hang': ['left_hung', 'left']}

        result = self.exp.run_statement("hang != 'left2'", variables=hang_variables)
        self.assertEqual(True, result)

    def test_equation_before_dot(self):
        variables = {'e_my_path': 'tom', 'tom.s': 'thomas'}

        result = self.exp.run_statement("e_my_path.s", variables=variables)
        self.assertEqual('thomas', result)
