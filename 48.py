sets_list = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]

result = set()

for s in sets_list:
    result.update(s)

print(result)
