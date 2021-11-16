import unittest

from expression_builder.expression_builder import ExpressionBuilder


class MathsOperationsTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_pi(self):
        result = self.exp.run_statement("result = PI")
        self.assertEqual(3.141592653589793, result['result'])

    def test_tan(self):
        result = self.exp.run_statement("result = tan(0.5)")
        self.assertEqual(0.5463024898437905, result['result'])

    def test_tand(self):
        result = self.exp.run_statement("result = tand(45)")
        self.assertEqual(1.0, round(result['result'], 5))

    def test_atan(self):
        result = self.exp.run_statement("result = atan(0.5)")
        self.assertAlmostEquals(0.46364760900080615, result['result'])

    def test_atand(self):
        result = self.exp.run_statement("result = atand(1.0)")
        self.assertEqual(45.0, result['result'])

    def test_cos(self):
        result = self.exp.run_statement("result = cos(0.5)")
        self.assertEqual(0.8775825618903728, result['result'])

    def test_cosd(self):
        result = self.exp.run_statement("result = cosd(60)")
        self.assertEqual(0.5, round(result['result'], 5))

    def test_acos(self):
        result = self.exp.run_statement("result = acos(0.5)")
        self.assertAlmostEquals(1.0471975511965976, result['result'])

    def test_acosd(self):
        result = self.exp.run_statement("result = acosd(0.5)")
        self.assertEqual(60.0, round(result['result'], 5))

    def test_sin(self):
        result = self.exp.run_statement("result = sin(0.5)")
        self.assertEqual(0.479425538604203, result['result'])

    def test_sind(self):
        result = self.exp.run_statement("result = sind(30)")
        self.assertEqual(0.5, round(result['result'], 5))

    def test_asin(self):
        result = self.exp.run_statement("result = asin(0.5)")
        self.assertAlmostEquals(0.5235987755982988, result['result'])

    def test_asind(self):
        result = self.exp.run_statement("result = asind(0.5)")
        self.assertEqual(30.0, round(result['result'], 5))

    def test_sqrt(self):
        result = self.exp.run_statement("result = sqrt(4)")
        self.assertEqual(2.0, result['result'])

    def test_sqrt_equation(self):
        result = self.exp.run_statement("result = sqrt((2+2))")
        self.assertEqual(2.0, result['result'])

    def test_hypot(self):
        result = self.exp.run_statement("result = hypot(9, 5)")
        self.assertEqual(10.29563, round(result['result'], 5))

    def test_int(self):
        result = self.exp.run_statement("result = int(1.3)")
        self.assertEqual(1, result['result'])
