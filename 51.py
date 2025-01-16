students_data = [
 {'name': 'Phúc', 'age': 20, 'score': 85},
 {'name': 'Thanh', 'age': 22, 'score': 75},
 {'name': 'Thản', 'age': 21, 'score': 90}
]

total_age = 0
total_score = 0
count = 0
res = {'average_score':None, 'average_age':None}

for c in students_data:
    total_age += c['age']
    total_score += c['score']
    count += 1

res['average_score'] = total_score/count
res['average_age'] = total_age/count

print(res)

