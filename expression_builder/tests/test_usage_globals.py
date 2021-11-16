import unittest

from expression_builder.expression_builder import ExpressionBuilder


class UsageGlobalTests(unittest.TestCase):
    # noinspection PyPep8Naming
    def setUp(self):
        self.data = {'ti': {'': {'name': 'Softwood'}, 'ladder': {'name': 'Hardwood'}, 'ladder:oak': {'name': 'OAK'}}}

    def test_usage_exist_single_level(self):
        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("ti", self.data['ti'])
        result = exp.run_statement("ti{'ladder'}.name")
        self.assertEqual("Hardwood", result)

    def test_doesnt_exist_single_level(self):
        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("ti", self.data['ti'])
        result = exp.run_statement("ti{'tom'}.name")
        self.assertEqual("Softwood", result)

    def test_usage_exist_2_levels(self):
        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("x_material.ti", self.data['ti'])
        result = exp.run_statement("x_material.ti{'ladder'}.name")
        self.assertEqual("Hardwood", result)

    def test_doesnt_exist_2_levels(self):

        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("x_material.ti", self.data['ti'])
        result = exp.run_statement("x_material.ti{'tom'}.name")
        self.assertEqual("Softwood", result)

    def test_usage_exist_multi_level(self):
        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("x_material.name.ti", self.data['ti'])
        result = exp.run_statement("x_material.name.ti{'ladder'}.name")
        self.assertEqual("Hardwood", result)

    def test_global_usage(self):
        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("x_material.ti", self.data['ti'])
        exp.add_to_global('u', 'ladder')
        result = exp.run_statement("x_material.ti{u}.name")
        self.assertEqual("Hardwood", result)

    def test_global_part_usage(self):
        exp = ExpressionBuilder()
        exp.add_to_global_usage_dict("x_material.ti", self.data['ti'])
        exp.add_to_global('u', 'ladder')
        exp.add_to_global('l', 'oak')
        result = exp.run_statement("x_material.ti{^'[u]:[l]'}.name")
        self.assertEqual("OAK", result)
