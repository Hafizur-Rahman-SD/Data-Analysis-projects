import unittest
import sea_level_predictor

class SeaLevelTestCase(unittest.TestCase):
    def test_plot_function_exists(self):
        self.assertTrue(hasattr(sea_level_predictor, 'draw_plot'),
                        msg="Function draw_plot is not defined.")
