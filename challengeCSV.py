import csv

fileName = "csvEx.txt"
accessMode = "r"

with open(fileName, accessMode) as myFile:
    data = csv.reader(myFile)

    for row in data:
        print(row)
        for v in row:
            print(v)