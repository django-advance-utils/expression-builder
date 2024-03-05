import unittest

from expression_builder.exceptions import ExpressionError, ExpressionVariableError
from expression_builder.expression_builder import ExpressionBuilder


class StringReplaceTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_to_global("fred", 1234)
        self.exp.add_to_global_string_statement("path", ";[tom];[tom]#")
        self.exp.add_to_global_string_statement("path2", ";[tom];[tom+$]#")

    def test_simple(self):
        result = self.exp.string_replace("fred")
        self.assertEqual('fred', result)

    def test_simple_math(self):
        result = self.exp.string_replace(";[1+5];#")
        self.assertEqual(';6;#', result)

    def test_simple_variable(self):
        result = self.exp.string_replace(";[tom];#", variables={'tom': 5})
        self.assertEqual(';5;#', result)

    def test_bool_variable_true(self):
        result = self.exp.string_replace(";[tom];#", variables={'tom': True})
        self.assertEqual(';1;#', result)

    def test_bool_variable_false(self):
        result = self.exp.string_replace(";[tom];#", variables={'tom': False})
        self.assertEqual(';0;#', result)

    def test_simple_variable2(self):
        result = self.exp.string_replace(";[tom];[tom]#", variables={'tom': 5})
        self.assertEqual(';5;5#', result)

    def test_simple_global_variable(self):
        result = self.exp.string_replace(";[fred];[fred]#")
        self.assertEqual(';1234;1234#', result)

    def test_string_variable(self):
        result = self.exp.string_replace(";[bill];#", {'bill': 'hello'})
        self.assertEqual(';hello;#', result)

    def test_unknown_variable(self):
        with self.assertRaises(ExpressionVariableError) as cm:
            self.exp.string_replace(";[tom];[tom]#")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'No variable named tom')

    def test_global(self):
        result = self.exp.run_statement("path", {'tom': 10})
        self.assertEqual(";10;10#", result)

    def test_global_with_replace(self):
        result = self.exp.run_statement("path2", {'tom': 10}, replace_values={'$': 5})
        self.assertEqual(";10;15#", result)

    def test_inline_replace(self):
        result = self.exp.run_statement('result = ^"ten = [ten]"', {'ten': 10})
        self.assertEqual("ten = 10", result['result'])
