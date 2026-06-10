import csv

with open("data_new.csv") as f:
    file_reader = csv.reader(f, delimiter=",")

    for row in file_reader:
        print(row)