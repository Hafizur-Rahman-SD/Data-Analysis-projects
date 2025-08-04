import unittest
import matplotlib
matplotlib.use('Agg')  # GUI backend for testing purposes

from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot 
##from time_series_visualizer module its very important to import the functions we want to test
import matplotlib.figure

class TestTimeSeriesVisualizer(unittest.TestCase):

    def test_line_plot(self): ## Test for line plot function
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
## Ensure that the plots are saved correctly
##this is the main function to run the tests
if __name__ == "__main__":
    unittest.main()
