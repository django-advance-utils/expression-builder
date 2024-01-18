import unittest

from expression_builder.expression_builder import ExpressionBuilder, ExpressionLog


class LogsTests(unittest.TestCase):

    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_none(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("10 + 10", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 20)

        self.assertEqual({}, expression_log.variables)
        self.assertEqual(['10 + 10'], expression_log.statements)

    def test_none2(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("result = 10 + 10", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result['result'], 20)

        self.assertEqual({}, expression_log.variables)
        self.assertEqual(['result = 10 + 10'], expression_log.statements)

    def test_vars(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("tom + b", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 7)

        self.assertEqual({'tom': 4, 'b': 3}, expression_log.variables)
        self.assertEqual(['tom[4] + b[3]'], expression_log.statements)

    def test_vars_no_space(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("tom+b", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 7)

        self.assertEqual({'tom': 4, 'b': 3}, expression_log.variables)
        self.assertEqual(['tom[4] + b[3]'], expression_log.statements)

    def test_brackets(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("tom + (b - c)", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 6)

        self.assertEqual({'tom': 4, 'b': 3, 'c': 1}, expression_log.variables)
        self.assertEqual(['tom[4] + (b - c)[2.0]', 'b[3] - c[1]'], expression_log.statements)

    def test_nested_brackets(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("tom + (b - c + (tom - b))", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 7)

        self.assertEqual({'tom': 4, 'b': 3, 'c': 1}, expression_log.variables)
        self.assertEqual(['tom[4] + (b - c + (tom - b))[3.0]',
                          'b[3] - c[1] + (tom - b)[1.0]',
                          'tom[4] - b[3]'], expression_log.statements)

    def test_double_brackets(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("tom + (b - c) + (tom - b)", variables={'tom': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 7)

        self.assertEqual({'tom': 4, 'b': 3, 'c': 1}, expression_log.variables)
        self.assertEqual(['tom[4] + (b - c)[2.0] + (tom - b)[1.0]',
                          'b[3] - c[1]', 'tom[4] - b[3]'], expression_log.statements)

    def test_question_mark1(self):
        expression_log = ExpressionLog()
        result = self.exp.run_statement("true?a:b",
                                        variables={'a': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 4)
        self.assertEqual({'a': 4, 'b': 3}, expression_log.variables)
        self.assertEqual(['true ? a[4] : b[3]'], expression_log.statements)

    def test_question_mark2(self):
        expression_log = ExpressionLog()
        result = self.exp.run_statement("a==b?a:b",
                                        variables={'a': 4, 'b': 3, 'c': 1},
                                        expression_log=expression_log)
        self.assertEqual(result, 3)
        self.assertEqual({'a': 4, 'b': 3}, expression_log.variables)
        self.assertEqual(['a[4] == b[3] ? a[4] : b[3]'], expression_log.statements)

    def test_function(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("sqrt(my_var)",
                                        variables={'my_var': 4},
                                        expression_log=expression_log)
        self.assertEqual(result, 2)

        self.assertEqual({'my_var': 4}, expression_log.variables)
        self.assertEqual(['sqrt(my_var)[2.0]', 'my_var[4]'], expression_log.statements)

    def test_string(self):
        expression_log = ExpressionLog()

        result = self.exp.run_statement("result = 'Hello World'",
                                        expression_log=expression_log)
        self.assertEqual(result['result'], 'Hello World')

        self.assertEqual({}, expression_log.variables)
        self.assertEqual(["result = 'Hello World'"], expression_log.statements)
