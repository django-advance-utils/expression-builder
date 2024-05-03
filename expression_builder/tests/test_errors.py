import unittest

from expression_builder.exceptions import ExpressionError, ExpressionVariableError
from expression_builder.expression_builder import ExpressionBuilder


class ErrorTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.vars = {'hello': 'hello world', 'empty_string': ''}

    def test_question_mark(self):
        with self.assertRaises(ExpressionError) as cm:
            self.exp.run_statement("result = 1?'sds'")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'Question mark not valid')

    def test_unknown_function(self):
        with self.assertRaises(ExpressionError) as cm:
            self.exp.run_statement("result = tom(1234)")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'No function named tom')

    def test_unknown_function2(self):
        with self.assertRaises(ExpressionError) as cm:
            self.exp.run_statement("result = tom('1234')")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'No function named tom')

    def test_unknown_variable(self):
        with self.assertRaises(ExpressionVariableError) as cm:
            self.exp.run_statement("result = tom")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'No variable named tom')

    def test_unknown_variable2(self):
        with self.assertRaises(ExpressionVariableError) as cm:
            self.exp.run_statement("result = 1?'tom")
        the_exception = cm.exception
        self.assertEqual(the_exception.value,  'No variable named tom')

    def test_bad_question_mark(self):
        with self.assertRaises(ExpressionError) as cm:
            self.exp.run_statement("result = 1'tom':'fred'")
        the_exception = cm.exception
        self.assertEqual(the_exception.value,  'Bad statement (result = 1\'tom\':\'fred\')')

    def test_blank(self):
        result = self.exp.run_statement("")
        self.assertEqual("", result)

    def test_none(self):
        # noinspection PyTypeChecker
        result = self.exp.run_statement(None)
        self.assertEqual("", result)

    def test_double_logic_statement(self):
        with self.assertRaises(ExpressionError) as cm:
            self.exp.run_statement("1 == 1;1 == 1;")
        the_exception = cm.exception
        self.assertEqual(the_exception.value,  'Bad statement (1 == 1;1 == 1;)')

    def test_different_types(self):
        with self.assertRaises(ExpressionError) as cm:
            self.exp.run_statement("result = hello == 15", variables=self.vars)
        the_exception = cm.exception
        self.assertEqual(the_exception.value,  'Different type compare (result = hello == 15)')

    def test_different_type_blank(self):
        # should not cause an error as the var is blank and will default to 0
        result = self.exp.run_statement("result = blank + 15", variables={'blank': ''})
        self.assertEqual({'result': 15}, result)

    def test_different_type_blank2(self):
        # should not cause an error as the var is blank and will default to 0
        result = self.exp.run_statement("result = 15 + blank", variables={'blank': ''})
        self.assertEqual({'result': 15}, result)

    def test_operations_error_tan(self):
        with self.assertRaises(ExpressionError) as cm:
            result = self.exp.run_statement("result = tan(blank)", variables={'blank': ''})
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'Value error (result = tan(blank))')
