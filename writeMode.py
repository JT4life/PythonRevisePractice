import csv

fileName = "csvEx.txt"
accessMode = "w"
file = open(fileName, accessMode)
file.write("Doyle McCarty, 27 \n")
file.write("Jodi Mills, 22 \n")
file.write("Nick Cage, 21 \n")
file.write("Saitama Mane, 30 \n")
file.write("Dicky Jones, 47 \n")

file.close()