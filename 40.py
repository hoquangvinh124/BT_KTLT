from random import randint

def create_random_ele_in_matrix(m, n):
    return [[randint(1, 100) for _ in range(n)] for _ in range(m)]

def output_row(matrix, row):
    print(matrix[row-1])

def output_column(matrix, column):
    print([row[column-1] for row in matrix])

def max_number(matrix):
    return max(max(row) for row in matrix)

def min_number(matrix):
    return min(min(row) for row in matrix)

def sort_zigzag(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            matrix[i].sort()
        else:
            matrix[i].sort(reverse=True)
    return matrix

m = int(input("Enter number of rows of matrix: "))
n = int(input("Enter number of columns of matrix: "))
matrix = create_random_ele_in_matrix(m, n)
print(matrix)

while True:
    print("\n1. Output row")
    print("2. Output column")
    print("3. Max number in matrix")
    print("4. Min number in matrix")
    print("5. Sort Matrix by zigzag row")
    print("0. Exit")

    choice = input("Enter your choice (0-5): ")

    if choice == '1':
        row = int(input("Enter row you want to output: "))
        output_row(matrix, row)
    elif choice == '2':
        column = int(input("Enter column you want to output: "))
        output_column(matrix, column)
    elif choice == '3':
        print("Max value:", max_number(matrix))
    elif choice == '4':
        print("Min value:", min_number(matrix))
    elif choice == '5':
        sorted_matrix = sort_zigzag(matrix)
        print("Matrix after zigzag sort:")
        for row in sorted_matrix:
            print(row)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
