students = [('Phúc', 85, 20), ('Diệu', 75, 22), ('Thanh', 85, 21), ('Thản', 80, 21)]

students = sorted(students, key=lambda x : (-x[1], x[2]))
print(students)