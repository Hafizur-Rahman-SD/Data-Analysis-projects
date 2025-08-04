import unittest
import matplotlib
matplotlib.use('Agg')  # GUI ছাড়া test চালানোর জন্য উপযুক্ত

from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import matplotlib.figure

class TestTimeSeriesVisualizer(unittest.TestCase):

    def test_line_plot(self):
        fig = draw_line_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        fig.savefig("test_line_plot_output.png")

    def test_bar_plot(self):
        fig = draw_bar_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        fig.savefig("test_bar_plot_output.png")

    def test_box_plot(self):
        fig = draw_box_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)
        fig.savefig("test_box_plot_output.png")

if __name__ == "__main__":
    unittest.main()
