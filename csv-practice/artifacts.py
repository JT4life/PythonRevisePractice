import csv
#artreader is a generator
with open('museum.csv', newline='') as csvfile:
    artreader = csv.DictReader(csvfile, delimiter='|')
    #turn it into a list
    rows = list(artreader)
    for row in rows[1:3]:
        print(row['country'])