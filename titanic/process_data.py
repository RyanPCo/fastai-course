import csv
import numpy

file = "./titanic/train.csv"

fields = []
data = []
rows = []

with open(file, "r") as csvfile:

    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)
