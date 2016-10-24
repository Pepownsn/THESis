## reading from a csv spreadsheet



# open csv file
with open(csv_file, 'rb') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
