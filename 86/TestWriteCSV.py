import csv
with open('employee.csv', mode='a+', encoding="utf8",newline='') as f:
    employee_writer = csv.writer(f, delimiter=',', quotechar='"')
    employee_writer.writerow(['5', 'Tú Linh', '02/02/2002'])
    employee_writer.writerow(['6', 'Nam Giao', '03/04/2000'])
    employee_writer.writerow(['7', 'Huỳnh Anh', '05/11/2001'])
