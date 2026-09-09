import csv

rows = [['name', 'age', 'occupation'],
        ['John', 28, 'Engineer'],
        ['Marie', 22, 'Designer'],
        ['Mike', 32, 'Doctor']]

file = open("_25_files/files/person.csv", "w")
csv_writer = csv.writer(file)

csv_writer.writerows(rows)
file.close()