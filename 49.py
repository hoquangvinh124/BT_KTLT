data = [('a', 10), ('b', 20), ('a', 30), ('c', 40)]

def change_to_dict(a):
    dic = {}
    for key, value in a:
        dic[key] = value + dic.get(key, 0)
    return dic

data = change_to_dict(data)

print(data)

