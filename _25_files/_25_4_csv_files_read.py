import csv

file = open("_25_files/files/person.csv", "r")
csv_dict_reader = csv.DictReader(file)

for row in csv_dict_reader:
    print(row["name"], row["age"], row["occupation"])

file.close()