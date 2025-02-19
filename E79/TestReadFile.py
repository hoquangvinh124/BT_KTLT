
from FileProcessing import *

arr_number = read_data('database_number.txt')
print(arr_number)

def print_negative_number_per_line(arr):
    for sub_arr in arr:
        for num in sub_arr:
            num = int(num)
            if num < 0:
                print(num, end='\t')
        print()

def print_smallest_number_per_line(arr):
    for sub_arr in arr:
        sub_arr = list(map(int, sub_arr))
        print(min(sub_arr))
    print()

def print_largest_number_per_line(arr):
    for sub_arr in arr:
        sub_arr = list(map(int, sub_arr))
        print(max(sub_arr))
    print()

def sort_number_per_line(arr):
    for i in range(len(arr)):
        if i % 2 != 0:
            new_arr = sorted(list(map(int, arr[i])), reverse=True)
            print(new_arr)
        else:
            new_arr = sorted(list(map(int, arr[i])))
            print(new_arr)
    print()

print("Negative Number per Line:")
print_negative_number_per_line(arr_number)
print("Smallest Number per Line:")
print_smallest_number_per_line(arr_number)
print("Largest Number per Line:")
print_largest_number_per_line(arr_number)
print("Sort Number:")
sort_number_per_line(arr_number)