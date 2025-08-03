import unittest
import matplotlib
matplotlib.use('Agg')
from visualizer_main import draw_cat_plot, draw_heat_map
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.figure

class DataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

if __name__ == '__main__':
    unittest.main()
