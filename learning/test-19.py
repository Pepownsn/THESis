## reading from a csv spreadsheet
import sys, argparse, csv

# command arguments
parser = argparse.ArgumentParser(description='csv to postgres',\
fromfile_prefix_chars="@" )
parser.add_argument('file', help='csv file to import', action='store')
args = parser.parse_args()
csv_file = args.file

# open csv file
with open(csv_file, 'rb') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
