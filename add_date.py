"""Add date

Usage:
    add_date.py <input_file> <output_file>
    add_date.py (-h | --help)
    add_date.py --version

Options:
    -h --help    Show this help.
    --version    Show version number.

"""
from docopt import docopt
import csv
import datetime


def excel_date(date1):
    """Turn a date object into an Excel date string """
    temp = datetime.datetime(1899 + 4, 12, 31)
    delta = date1 - temp
    return float(delta.days) + (float(delta.seconds) / 86400)


def add_date(input_file, output_file):
    """Add a datetime string to the CSV

    @TODO - Add an argument to the script to pass the input and output files
    """
    with open(input_file, 'r') as csvinput:
        with open(output_file, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\r')
            reader = csv.reader(csvinput)

            all = []
            # Skip the headers
            for _ in xrange(3):
                next(reader)
            for row in reader:
                row_year = row[1]
                day_of_year = row[2]
                minutes_of_day = row[3]
                year_start = datetime.datetime(int(row_year), 1, 1)
                day_delta = datetime.timedelta(int(day_of_year) - 1, minutes=int(minutes_of_day))
                #row_date = year_start + day_delta
                row_date = excel_date(year_start + day_delta)
                print row_date
                row.insert(4, row_date)

                all.append(row)

            writer.writerows(all)


if __name__ == "__main__":
    args = docopt(__doc__, version='Add Date 0.1')
    add_date(args['<input_file>'], args['<output_file>'])
