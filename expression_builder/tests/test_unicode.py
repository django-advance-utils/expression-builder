import unittest

from expression_builder.expression_builder import ExpressionBuilder


class UnicodeTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()
        self.exp.add_to_global("fred", 'hello', inheritance_level=1)
        self.exp.add_to_global("william", u'hello', inheritance_level=2)

    def test_unicode_vars(self):
        result = self.exp.run_statement("fred == william;")
        self.assertEqual(True, result)

    def test_unicode_inputs(self):
        result = self.exp.run_statement(u"fred == fred;")
        self.assertEqual(True, result)