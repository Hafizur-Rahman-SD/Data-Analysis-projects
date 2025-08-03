import unittest
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Backend set for testing without GUI
import matplotlib.pyplot as plt

from Page_View_Time_Series_Visualizer import draw_cat_plot, draw_heat_map

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

        # Check that the number of rows is correct after filtering
        df_clean = df[
            (df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))
        ]
        self.assertTrue(len(df_clean) > 1200, "Cleaned data should have more than 1200 rows")

class PlotTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig, "draw_cat_plot should return a figure.")
        self.assertIsInstance(fig, matplotlib.figure.Figure, "Output should be a matplotlib figure.")
        fig.savefig("test_cat_plot_output.png")  # Optional: save test output

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig, "draw_heat_map should return a figure.")
        self.assertIsInstance(fig, matplotlib.figure.Figure, "Output should be a matplotlib figure.")
        fig.savefig("test_heat_map_output.png")  # Optional: save test output

if __name__ == '__main__':
    unittest.main()
