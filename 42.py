data = [(1, 2), (2, 3), (3, 4), (1, 2)]
unique = set()

for t in data:
    for ele in t:
        unique.add(ele)

print(list(unique))