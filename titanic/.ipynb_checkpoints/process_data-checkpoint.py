import csv
import numpy as np

file = "./titanic/train.csv"

fields = []
rows = []

with open(file, "r") as csvfile:

    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

print(fields)

for x in rows:
    if (x[5] == "" or x[11] == ""):
        rows.remove(x)
    else:
        x.pop(10)
        x.pop(8)
        x.pop(3)
        x.pop(0)
