def statistics(t):
    number_of_list = len(t)
    total = sum(t)
    mean = total / number_of_list
    min_value = min(t)
    max_value = max(t)
    return number_of_list, total, mean, min_value, max_value

inp = tuple(map(float, input("Nhap chuoi cac day so: ").split(",")))
print(inp)
number_of_list, total, mean, min_value, max_value = statistics(inp)
print(f"Count={number_of_list}")
print(f"Total={total}")
print(f"Average={mean}")
print(f"Max Value={min_value}")
print(f"Min Value={max_value}")