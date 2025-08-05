import unittest
from sea_level_predictor import draw_plot  # jodi main code 'sea_level_predector.py' file e thake

class TestSeaLevelPlot(unittest.TestCase):
    def test_draw_plot(self):
        ax = draw_plot()
        # Check j axis object thik ache kina
        self.assertIsNotNone(ax)
        # Check x axis label thik ache kina
        self.assertEqual(ax.get_xlabel(), 'Year')
        # Check y axis label thik ache kina
        self.assertEqual(ax.get_ylabel(), 'Sea Level (inches)')
        # Check title thik ache kina
        self.assertEqual(ax.get_title(), 'Rise in Sea Level')

if __name__ == '__main__': ##main function run kore eta chara code output dibe na 
    unittest.main()
