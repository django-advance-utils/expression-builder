import unittest

from expression_builder.expression_builder import ExpressionBuilder


class OptionsTest(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_option("option_simple", [['tom == 1', 100],
                                              ['tom == 2', 200],
                                              ['tom == 20', 2000]],
                            default_value=999)

        self.exp.add_option("option_2_levels", [['tom == 1', [['dave == 9', 100],
                                                              ['dave == 8', 200]]],
                                                ['tom == 2', 300]],
                            default_value=999)

        self.exp.add_option('ladder_path',
                            [['v_ladder_required=="yes" && q_integrated_applied_drip=="applied"',
                              [['q_ladder_joint_method=="butted"',
                                [['q_ladder_style=="a"', '"p_ladder_a"'],
                                 ['q_ladder_style=="b"', '"p_ladder_b"'],
                                 ['q_ladder_style=="c"', '"p_ladder_c"'],
                                 ['q_ladder_style=="d"', '"p_ladder_d"']]],
                               ['q_ladder_joint_method=="rebated"',
                                [['q_ladder_style=="a"', '"p_ladder_e"'],
                                 ['q_ladder_style=="b"', '"p_ladder_f"'],
                                 ['q_ladder_style=="c"', '"p_ladder_g"'],
                                 ['q_ladder_style=="d"', '"p_ladder_h"']]],
                               ['q_ladder_joint_method=="tongued"',
                                [['q_ladder_style=="a"', '"p_ladder_i"'],
                                 ['q_ladder_style=="b"', '"p_ladder_j"'],
                                 ['q_ladder_style=="c"', '"p_ladder_k"'],
                                 ['q_ladder_style=="d"', '"p_ladder_l"']]]]]],
                            default_value='"p_ladder_a"')

        self.exp.add_option('box_data',
                            [['v_box == 1',
                              {'head': {'vw': '100+v_box',
                                        'vt': 123},
                               'jamb': {'vw': 'A',
                                        'vt': 'B'}},
                              {'A': 100,
                               'B': 123}
                              ],
                             ['v_box == 2',
                              {'head': {'vw': 90,
                                        'vt': 95},
                               'jamb': {'vw': 91,
                                        'vt': 96}},
                              {'A': 1,
                               'B': 2}
                              ],
                             ],
                            default_value={'head': {'vw': 80,
                                                    'vt': 85},
                                           'jamb': {'vw': 81,
                                                    'vt': 86}})

    def test_simple_default(self):
        result = self.exp.run_statement("option_simple", variables={'tom': 0})
        self.assertEqual(999, result)

    def test_simple_one(self):
        result = self.exp.run_statement("option_simple", variables={'tom': 1})
        self.assertEqual(100, result)

    def test_simple_two(self):
        result = self.exp.run_statement("option_simple", variables={'tom': 1})
        self.assertEqual(100, result)

    def test_level2_default(self):
        result = self.exp.run_statement("option_2_levels", variables={'tom': 0, 'dave': 0})
        self.assertEqual(999, result)

    def test_level2_default2(self):
        result = self.exp.run_statement("option_2_levels", variables={'tom': 1, 'dave': 0})
        self.assertEqual(999, result)

    def test_level2_one(self):
        result = self.exp.run_statement("option_2_levels", variables={'tom': 1, 'dave': 9})
        self.assertEqual(100, result)

    def test_level2_two(self):
        result = self.exp.run_statement("option_2_levels", variables={'tom': 1, 'dave': 8})
        self.assertEqual(200, result)

    def test_level2_three(self):
        result = self.exp.run_statement("option_2_levels", variables={'tom': 2, 'dave': 0})
        self.assertEqual(300, result)

    def test_ladder(self):
        result = self.exp.run_statement("ladder_path", variables={'v_ladder_required': 'yes',
                                                                  'q_integrated_applied_drip': 'applied',
                                                                  'q_ladder_joint_method': 'rebated',
                                                                  'q_ladder_style': 'c'})
        self.assertEqual('"p_ladder_g"', result)

    def test_ladder_default(self):
        result = self.exp.run_statement("ladder_path", variables={'v_ladder_required': 'no',
                                                                  'q_integrated_applied_drip': 'applied',
                                                                  'q_ladder_joint_method': 'rebated',
                                                                  'q_ladder_style': 'c'})
        self.assertEqual('"p_ladder_a"', result)

    def test_ladder2(self):
        result = self.exp.run_statement("ladder_path", variables={'v_ladder_required': 'yes',
                                                                  'q_integrated_applied_drip': 'applied',
                                                                  'q_ladder_joint_method': 'tongued',
                                                                  'q_ladder_style': 'a'})
        self.assertEqual('"p_ladder_i"', result)

    def test_box_test_1(self):
        result = self.exp.run_statement("box_data", variables={'v_box': 1})
        self.assertEqual({'head': {'vt': 123, 'vw': 101.0},
                          'jamb': {'vt': 123, 'vw': 100}}, result)
