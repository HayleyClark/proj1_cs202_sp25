import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    #emission_per_capita tests
    def test_emissions_per_capita_normal(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Test", "other"), 2020, 3, 100.0)
        self.assertAlmostEqual(emissions_per_capita(rc), 33.3333, places=4)

    def test_emissions_per_capita_zero_population(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Test", "other"), 2020, 0, 200.0) 
        self.assertEqual(emissions_per_capita(rc), 0.0)

    def test_emissions_per_capita_zero_emissions(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Test", "other"), 2020, 100, 0.0) 
        self.assertEqual(emissions_per_capita(rc), 0.0)

    #area tests
    def test_area_normal(self):
        gr = GlobeRect(0, 1, 0, 1)
        result = area(gr)
        self.assertTrue(result > 0)

    def test_area_zero_height(self):
        gr = GlobeRect(5, 5, 10, 20)
        self.assertEqual(area(gr), 0.0)

    def test_area_zero_weidth(self):
        gr = GlobeRect(0, 10, 50, 50)
        self.assertEqual(area(gr), 0.0)

    def test_area_crosses_date_line(self):
        gr = GlobeRect(10, 20, 170, -170)
        result = area(gr)
        self.assertTrue(result > 0)

    #emissions_per_square_kilometer tests
    def test_emissions_per_square_kilometer_normal(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Test", "other"), 2020, 100, 100.0)
        result = emissions_per_square_kilometer(rc)
        self.assertTrue(result > 0)

    def test_emissions_per_square_kilometer_zero_area(self):
        rc = RegionCondition(Region(GlobeRect(5, 5, 10, 20), "Test", "other"), 2020, 100, 100.0)
        self.assertEqual(emissions_per_square_kilometer(rc), 0.0)
    
    #densest tests
    def test_densest_normal(self):
        rc1 = RegionCondition(Region(GlobeRect(0, 10, 0, 10), "LowDensity", "other"), 2020, 100, 50.0)
        rc2 = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "HighDensity", "other"), 2020, 1000000, 50.0)
        self.assertEqual(densest([rc1, rc2]), "HighDensity")

    def test_densest_single_item(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "OnlyRegion", "other"), 2020, 100, 50.0)
        self.assertEqual(densest([rc]), "OnlyRegion")

    def test_densest_tie(self):
        rc1 = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "First", "other"), 2020, 100, 50.0)
        rc2 = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Second", "other"), 2020, 100, 50.0)
        self.assertEqual(densest([rc1, rc2]), "First")

    #project_condition tests
    def test_project_condition_growth(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Test", "other"), 2020, 1000, 100.0)
        result = project_condition(rc, 10)
        self.assertTrue(result.pop > 1000)
        self.assertEqual(result.year, 2030)

    def test_project_condition_zero_population(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "Test", "other"), 2020, 0, 100.0)
        result = project_condition(rc, 5)
        self.assertEqual(result.pop, 0)
        self.assertEqual(result.ghg_rate, 0.0)

    def test_project_condition_forest_decrease(self):
        rc = RegionCondition(Region(GlobeRect(0, 1, 0, 1), "ForestRegion", "forest"), 2020, 1000, 100.0)
        result = project_condition(rc, 10)
        self.assertTrue(result.pop < 1000)


if __name__ == '__main__':
    unittest.main()
