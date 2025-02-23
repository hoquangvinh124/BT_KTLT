import csv
import os

class CSVFileFactory:
    @staticmethod
    def write_data(arr_data, filename):
        fieldnames = list(arr_data[0].__dict__.keys())
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in arr_data:
                writer.writerow(item.__dict__)
    @staticmethod
    def read_data(filename, ClassName):
        if not os.path.isfile(filename):
            return []
        arr_data = []
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                obj = ClassName(**row)
                arr_data.append(obj)
        return arr_data