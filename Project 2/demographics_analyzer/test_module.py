# test_module.py

import unittest
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_calculate_demographic_data(self):
        result = calculate_demographic_data()

        # Test 1: Check if total number of each race is correct
        self.assertIn("race_count", result)
        self.assertIsInstance(result["race_count"], pd.Series)

        # Test 2: Check average age of men is a float
        self.assertIn("average_age_men", result)
        self.assertIsInstance(result["average_age_men"], float)

        # Test 3: Check percentage with Bachelor's degree is float
        self.assertIn("percentage_bachelors", result)
        self.assertIsInstance(result["percentage_bachelors"], float)

        # You can add more specific value-based tests here if needed

if __name__ == "__main__":
    unittest.main()
