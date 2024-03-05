import unittest

from expression_builder.exceptions import ExpressionError, ExpressionVariableError
from expression_builder.expression_builder import ExpressionBuilder


class SymbolicLinkTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.exp = ExpressionBuilder()

    def test_link1(self):
        exp = ExpressionBuilder()
        exp.add_to_global('i_ladder.vw', 195)
        exp.add_symbolic_link_global('ladder', 'i_ladder.vw')
        result = exp.run_statement("ladder")
        self.assertEqual(195, result)

    def test_clear_link1(self):
        exp = ExpressionBuilder()
        exp.add_to_global('i_ladder.vw', 195)
        exp.add_symbolic_link_global('ladder', 'i_ladder.vw')

        exp.clear_all_symbolic_link_global()

        with self.assertRaises(ExpressionVariableError) as cm:
            self.exp.run_statement("ladder")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'No variable named ladder')

    def test_link_category(self):
        exp = ExpressionBuilder()
        exp.add_to_global('i_ladder.vw', 195)
        exp.add_symbolic_link_global('ladder', 'i_ladder.vw', 'test')
        result = exp.run_statement("ladder")
        self.assertEqual(195, result)

    def test_clear_category(self):
        exp = ExpressionBuilder()
        exp.add_to_global('i_ladder.vw', 195)
        exp.add_to_global('i_box.vw', 200)
        exp.add_symbolic_link_global('ladder', 'i_ladder.vw', 'test')
        exp.add_symbolic_link_global('box', 'i_box.vw')

        exp.clear_all_symbolic_link_global('test')

        with self.assertRaises(ExpressionVariableError) as cm:
            self.exp.run_statement("ladder")
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 'No variable named ladder')
        result = exp.run_statement("box")
        self.assertEqual(200, result)
