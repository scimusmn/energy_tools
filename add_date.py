"""Add date

Usage:
    add_date.py <input_file> <output_file>
    add_date.py (-h | --help)
    add_date.py --version

Options:
    -h --help    Show this help.
    --version    Show version number.

@TODO - This is not tested yet
"""
from docopt import docopt
import csv
import datetime


def excel_date(date1):
    temp = datetime.datetime(1899 + 4, 12, 30)
    delta = date1 - temp
    return float(delta.days) + (float(delta.seconds) / 86400)


"""Add a datetime string to the CSV

@TODO - Add an argument to the script to pass the input and output files
"""


def add_date():
    with open('15_int.csv', 'r') as csvinput:
        with open('15_int_date.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\r')
            reader = csv.reader(csvinput)

            all = []
            for row in reader:
                row_year = row[1]
                day_of_year = row[2]
                minutes_of_day = row[3]
                year_start = datetime.datetime(int(row_year), 1, 1)
                day_delta = datetime.timedelta(int(day_of_year) - 1, minutes=int(minutes_of_day))
                row_date = year_start + day_delta
                print row_date
                row.insert(4, row_date)

                all.append(row)

            writer.writerows(all)


if __name__ == "__main__":
    args = docopt(__doc__, version='Add Date 0.1')
    add_date(args['<input_file>'], args['<output_file>'])
