import random

def random_list():
    return [random.randint(-100, 100) for _ in range(10)]

def add_element(lst, element):
    lst.append(element)
    return lst

def count(lst, k):
    return lst.count(k)

def is_perfect_number(n):
    if n <= 0:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def sum_perfect_numbers(lst):
    return sum(num for num in lst if is_perfect_number(num))

def sort_list(lst):
    return sorted(lst)

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

def delete_element(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

def delete_negative_numbers(lst):
    return [num for num in lst if num >= 0]

def delete_entire_list(lst):
    lst.clear()
    return lst


rl = random_list()

while True:
    print(rl)
    print("1. Add element")
    print("2. Count occurrences of k")
    print("3. Calculate sum of perfect numbers")
    print("4. Sort ascending")
    print("5. Sort descending")
    print("6. Delete specific element")
    print("7. Delete negative numbers")
    print("8. Delete entire list")
    print("0. Exit")

    choice = input("Enter your choice (0-9): ")

    if choice == '0':
        break
    elif choice == '1':
        element = int(input("Enter element to add: "))
        add_element(rl, element)
    elif choice == '2':
        k = int(input("Enter k: "))
        print(f"{k} appears {count(rl, k)} times")
    elif choice == '3':
        print(f"Sum of perfect numbers: {sum_perfect_numbers(rl)}")
    elif choice == '4':
        rl = sort_list(rl)
    elif choice == '5':
        rl = sort_list_descending(rl)
    elif choice == '6':
        element = int(input("Enter element to delete: "))
        rl = delete_element(rl, element)
    elif choice == '7':
        rl = delete_negative_numbers(rl)
    elif choice == '8':
        rl = delete_entire_list(rl)
