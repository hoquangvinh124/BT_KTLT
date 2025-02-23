import openpyxl
from StudentClass import Student

class ExcelManager:
    def __init__(self, filename):
        self.filename = filename

    def read_excel(self):
        workbook = openpyxl.load_workbook(self.filename)
        sheet = workbook.active
        data_rows = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            obj = Student(row[0],row[1],row[2],row[3],row[4])
            data_rows.append(obj)
        return data_rows
