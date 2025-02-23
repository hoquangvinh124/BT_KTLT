import csv
with open('employee.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(' - '.join(row))
