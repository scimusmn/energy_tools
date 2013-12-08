"""Graph CSV energy data

Usage:
    graph.py <input_file>
    graph.py (-h | --help)
    graph.py --version

Options:
    -h --help    Show this help.
    --version    Show version number.

"""
from docopt import docopt
import csv
import matplotlib
import pylab


def getColumn(filename, column):
    o = open(filename, 'rU')
    results = csv.reader(o)
    print results
    #results = csv.reader(open("data_2004-2013.csv"), delimiter="\t")
    return [result[column] for result in results]


def make_graph(input_file):
    reader = csv.reader(open(input_file, 'rU'))
    date = []
    buy = []

    for _ in xrange(3):
        next(reader)

    for line in reader:
        # Convert ISO datetime to Python date
        python_datetime = dateutil.parser.parse(line[4])
        # Convert Python datetime to MatPlotLib format
        matplotlib_datetime = mdates.date2num(python_datetime)
        # Add date and values to graph data set
        date.append(matplotlib_datetime)
        buy.append(line[5])

    matplotlib.pyplot.scatter(date, buy)


if __name__ == "__main__":
    args = docopt(__doc__, version='Graph 0.1')
    make_graph(args['<input_file>'])
