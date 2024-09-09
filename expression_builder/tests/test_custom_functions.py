import unittest

from expression_builder.expression_builder import ExpressionBuilder


class MyExpressionBuilder(ExpressionBuilder):
    def convert_functions(self, function_name, arguments):

        if function_name == "test":
            return {'value': {'type': 'foo', 'name': 'bar', 'value': 123}, 'routine': False}

        else:
            return super().convert_functions(function_name, arguments)


class CustomFunctionsTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = MyExpressionBuilder()

    def test_get_int_value(self):
        result = self.exp.run_statement("test()")
        self.exp.add_to_global('r', result)
        self.assertEqual({'name': 'bar', 'type': 'foo', 'value': 123}, result)

        self.assertEqual(self.exp.run_statement("get(r,'value')"), 123)
        self.assertEqual(self.exp.run_statement("r.value"), 123)

    def test_get_string_value(self):
        result = self.exp.run_statement("test()")
        self.exp.add_to_global('r', result)
        self.assertEqual({'name': 'bar', 'type': 'foo', 'value': 123}, result)

        self.assertEqual(self.exp.run_statement("get(r,'name')"), 'bar')
        self.assertEqual(self.exp.run_statement("r.name"), 'bar')
