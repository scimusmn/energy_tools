"""Graph a very simple list of digits

This is an example script so that I can learn how to use MatPlotLib

Usage:
    graph_simple.py [-h | --help]
    graph_simple.py --version

Options:
    -h --help    Show this help.
    --version    Show version number.

"""
from docopt import docopt
import matplotlib
import pylab


def make_graph():
    x = [1, 2, 3, 4]
    y = [3, 4, 8, 6]
    matplotlib.pyplot.scatter(x, y)
    matplotlib.pyplot.show()

if __name__ == "__main__":
    args = docopt(__doc__, version='Graph Simple 0.1')
    make_graph()
