def calculate(obj):
    Total = 0
    for t in obj:
        sum = 0
        print(t)
        for v in range(1, len(t), 2):
            if t[v] % 2 == 0:
                sum += t[v]
        print(f"Sum of t={sum}")
        Total += sum
    print(f"Sum all={Total}")


numbers_list = [(1, 2, 3, 4), (5, 13, 7, 8), (9, 10, 11, 12)]
calculate(numbers_list)