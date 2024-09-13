import unittest

from expression_builder.expression_builder import ExpressionBuilder


class StringOperationsTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_contains_true(self):
        result = self.exp.run_statement("contains('app','apple')")
        self.assertEqual(True, result)

    def test_contains_false(self):
        result = self.exp.run_statement("contains('banana','apple')")
        self.assertEqual(False, result)

    def test_not_contains_true(self):
        result = self.exp.run_statement("not_contains('banana','apple')")
        self.assertEqual(True, result)

    def test_not_contains_false(self):
        result = self.exp.run_statement("not_contains('app','apple')")
        self.assertEqual(False, result)

    def test_begins_with_true(self):
        result = self.exp.run_statement("begins_with('app','apple')")
        self.assertEqual(True, result)

    def test_begins_with_false(self):
        result = self.exp.run_statement("begins_with('ban','apple')")
        self.assertEqual(False, result)

    def test_not_begins_with_true(self):
        result = self.exp.run_statement("not_begins_with('ban','apple')")
        self.assertEqual(True, result)

    def test_not_begins_with_false(self):
        result = self.exp.run_statement("not_begins_with('app','apple')")
        self.assertEqual(False, result)

    def test_ends_with_true(self):
        result = self.exp.run_statement("ends_with('ple','apple')")
        self.assertEqual(True, result)

    def test_ends_with_false(self):
        result = self.exp.run_statement("ends_with('ban','apple')")
        self.assertEqual(False, result)

    def test_not_ends_with_true(self):
        result = self.exp.run_statement("not_ends_with('ban','apple')")
        self.assertEqual(True, result)

    def test_not_ends_with_false(self):
        result = self.exp.run_statement("not_ends_with('ple','apple')")
        self.assertEqual(False, result)

    # Case-insensitive tests
    def test_icontains_true(self):
        result = self.exp.run_statement("icontains('app','Apple')")
        self.assertEqual(True, result)

    def test_icontains_false(self):
        result = self.exp.run_statement("icontains('banana','Apple')")
        self.assertEqual(False, result)

    def test_ibegins_with_true(self):
        result = self.exp.run_statement("ibegins_with('app','Apple')")
        self.assertEqual(True, result)

    def test_ibegins_with_false(self):
        result = self.exp.run_statement("ibegins_with('ban','Apple')")
        self.assertEqual(False, result)

    def test_iends_with_true(self):
        result = self.exp.run_statement("iends_with('ple','Apple')")
        self.assertEqual(True, result)

    def test_iends_with_false(self):
        result = self.exp.run_statement("iends_with('ban','Apple')")
        self.assertEqual(False, result)

    def test_iequal_true(self):
        result = self.exp.run_statement("iequal('apple','Apple')")
        self.assertEqual(True, result)

    def test_iequal_false(self):
        result = self.exp.run_statement("iequal('apple','Banana')")
        self.assertEqual(False, result)

