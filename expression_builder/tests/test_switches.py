import unittest

from expression_builder.expression_builder import ExpressionBuilder


class SwitchTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_case1(self):
        result = self.exp.run_statement(
                "switch(tom){case 1: 10; break; case 2: 20; break; default: -1}", variables={'tom': 1})
        self.assertEqual(10, result)

    def test_case2(self):
        result = self.exp.run_statement(
                "switch(tom){case 1: 10; break; case 2: 20; break; default: -1}", variables={'tom': 2})
        self.assertEqual(20, result)

    def test_default(self):
        result = self.exp.run_statement(
                "switch(tom){case 1: 10; break; case 2: 20; break; default: -1}", variables={'tom': 10})
        self.assertEqual(-1, result)

    def test_case1_result_start(self):
        result = self.exp.run_statement(
                "result = switch(tom){case 1: 10; break; case 2: 20; break; default: -1}", variables={'tom': 1})
        self.assertEqual(10, result['result'])

    def test_case1_result_in(self):
        result = self.exp.run_statement(
            "switch(tom){case 1: result=10; break; case 2: result=20; break; default: result=-1}",
            variables={'tom': 1})
        self.assertEqual(10, result['result'])

    def test_string(self):
        result = self.exp.run_statement(
            "switch(tom){case 'abc': 10; break; case 'fred': 20; break; default: -1}",
            variables={'tom': 'fred'})
        self.assertEqual(20, result)

    def test_string_back(self):
        result = self.exp.run_statement(
            "switch(tom){case 'a': 'apple'; break; case 'b': 'banana'; break; default: 'nothing}",
            variables={'tom': 'a'})
        self.assertEqual('apple', result)

    def test_string_back2(self):
        result = self.exp.run_statement(
            "switch(tom){case 'a': 'apple'; break; case 'b': 'ba{nana'; break; default: 'nothing}",
            variables={'tom': 'b'})
        self.assertEqual('ba{nana', result)

    def test_string_silly(self):
        result = self.exp.run_statement(
            """switch(tom){case 'a': 'case "b": "no"'; break; case 'b': 'yes'; break; default: 'nothing}""",
            variables={'tom': 'b'})
        self.assertEqual('yes', result)

    def test_no_default(self):
        result = self.exp.run_statement(
            "switch(tom){case 1: 10; break; case 2: 20; break;}",
            variables={'tom': 10})
        self.assertEqual('', result)

    def test_double_switch(self):
        result = self.exp.run_statement(
            "switch(tom){case 1: switch(bill){case 1: 10; break; case 2: 200 }; break; case 2: 20; break;}",
            variables={'tom': 1, 'bill': 2})
        self.assertEqual(200, result)

    def test_no_break(self):
        result = self.exp.run_statement(
            "switch(tom){case 1: case 2: result=20;",
            variables={'tom': 1})
        self.assertEqual(20, result['result'])

    def test_no_break2(self):
        result = self.exp.run_statement(
            "switch(tom){case 1: result=10; case 2: result=20;",
            variables={'tom': 1})
        self.assertEqual(20, result['result'])

    def test_ladder_type(self):
        result = self.exp.run_statement(
            "switch(1){case 1: 'p_ladder'; break; case2: 'p_ladder_flush'; break; case 3: 'p_ladder_jointed'}")
        self.assertEqual('p_ladder', result)

