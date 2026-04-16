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

    #
    def test_holder(self):
        pass


if __name__ == '__main__':
    unittest.main()
