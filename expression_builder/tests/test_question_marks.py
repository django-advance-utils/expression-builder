import unittest

from expression_builder.expression_builder import ExpressionBuilder


class QuestionMarkTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.vars = {'tom': 30, 'fred': 3, 'tommy': 66, 'i_fc': 'no', 'opening_type': 'N'}

    def test_basic_t(self):
        result = self.exp.run_statement("result = true?10:20;")
        self.assertEqual(10, result['result'])

    def test_basic_f(self):
        result = self.exp.run_statement("result = false?10:20;")
        self.assertEqual(20, result['result'])

    def test_basic_t2(self):
        result = self.exp.run_statement("true?10:20;")
        self.assertEqual(10, result)

    def test_basic_f2(self):
        result = self.exp.run_statement("false?10:20;")
        self.assertEqual(20, result)

    def test_basic_f_space(self):
        result = self.exp.run_statement("result = false? 10: 20;")
        self.assertEqual(20, result['result'])

    def test_basic_t3(self):
        result = self.exp.run_statement("result = tom==30?10:20;", variables=self.vars)
        self.assertEqual(10, result['result'])

    def test_basic_f3(self):
        result = self.exp.run_statement("result = tom==31?10:20;", variables=self.vars)
        self.assertEqual(20, result['result'])

    def test_basic_add(self):
        result = self.exp.run_statement("result = 10+(tom==31?10:20);", variables=self.vars)
        self.assertEqual(30, result['result'])

    def test_basic_double_t(self):
        result = self.exp.run_statement("result = tom==30?false?100:150:true?200:250;", variables=self.vars)
        self.assertEqual(150, result['result'])

    def test_basic_double_f(self):
        result = self.exp.run_statement("result = tom==31?false?100:150:true?200:250;", variables=self.vars)
        self.assertEqual(200, result['result'])

    def test_basic_double_f2(self):
        result = self.exp.run_statement("result = tom==31?false?100:150:false?200:250;", variables=self.vars)
        self.assertEqual(250, result['result'])

    def test_bracket(self):
        result = self.exp.run_statement("(0 > 0)?300:200;", variables=self.vars)
        self.assertEqual(200, result)

    def test_save_in_true(self):
        result = self.exp.run_statement("true?a=100:200", variables=self.vars)
        self.assertEqual(100, result['a'])

    def test_save_in_false(self):
        result = self.exp.run_statement("false?a=100:200", variables=self.vars)
        self.assertEqual(200, result)

    def test_string(self):
        exp = ExpressionBuilder()
        exp.add_to_global('opening_type', 'N')
        result = exp.run_statement("(opening_type=='N' && i_fc=='no')?'glazing':'casement'", {'i_fc': 'no'})
        self.assertEqual('glazing', result)

    def test_double_save_in_true(self):
        result = self.exp.run_statement("true?(a=100;b=200):250", variables=self.vars)
        self.assertEqual(100, result['a'])
        self.assertEqual(200, result['b'])

    def test_double_save_in_false(self):
        result = self.exp.run_statement("false?200:(a=100;b=200)", variables=self.vars)
        self.assertEqual(100, result['a'])
        self.assertEqual(200, result['b'])

    def test_double_save_in_both(self):
        result = self.exp.run_statement("true?(a=120;b=220):(a=100;b=200)", variables=self.vars)
        self.assertEqual(120, result['a'])
        self.assertEqual(220, result['b'])

    def test_complex(self):
        local_vars = {'q_box': 'Type 6',
                      'i_ladder_backing_cover_vw': '160',
                      'q_ladder_case_backing': 'Flush',
                      'b_box_ladder': 166,
                      'v_outer_lining_overlap': 6,
                      'v_ladder_outer_lining_defined_width': 160}
        statement = '((q_box=="Type 1" || q_box=="Type 4") && q_ladder_case_backing=="Flush")?' \
                    ' i_ladder_backing_cover_vw:(q_box=="Type 3")? b_box_ladder + v_outer_lining_overlap ' \
                    ' - v_ladder_outer_lining_defined_width:(q_box=="Type 6")? b_box_ladder - ' \
                    'v_ladder_outer_lining_defined_width:0'
        result = self.exp.run_statement(statement, variables=local_vars)
        self.assertEqual(6, result)
