import numpy as np

def generate_matrix(rows, cols):
    return np.random.randint(-100, 101, (rows, cols))

def calculate_determinant(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        return np.linalg.det(matrix)
    return "Chỉ ma trận vuông mới có định thức hoi"

def find_inverse(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        try:
            return np.linalg.inv(matrix)
        except ValueError:
            return "Ma trận kỳ dị không có định thức"
    return "Chỉ có ma trận vuông mới có ma trận khả nghịch."

def sort_matrix_by_row(matrix):
    return np.sort(matrix, axis=1)

def sort_matrix_by_column(matrix):
    return np.sort(matrix, axis=0)

def sort_by_row_average(matrix):
    row_means = np.mean(matrix, axis=1)
    return matrix[np.argsort(row_means)]

def change_matrix_value(matrix, row, col, new_value):
    matrix[row, col] = new_value
    return matrix

def increase_column_value(matrix, col_index):
    matrix[:, col_index] += 2
    return matrix

def add_vector_to_rows(matrix, vector):
    if len(vector) == matrix.shape[1]:
        return matrix + vector
    return "Vecto phải cùng với số cột"

def calculate_matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def calculate_svd(matrix):
    U, S, V = np.linalg.svd(matrix)
    return U, S, V

def print_menu():
    print("1. Tính định thức ma trận")
    print("2. Tìm ma trận nghịch đảo")
    print("3. Sắp xếp ma trận theo hàng")
    print("4. Sắp xếp ma trận theo cột")
    print("5. Sắp xếp ma trận theo giá trị trung bình của hàng")
    print("6. Thay đổi giá trị một phần tử trong ma trận")
    print("7. Tăng giá trị một cột lên 2")
    print("8. Cộng vector vào từng hàng của ma trận")
    print("9. Tính hạng của ma trận")
    print("10. Tính SVD (Singular Value Decomposition)")
    print("11. Thoát chương trình")

def main():
    rows = int(input("Nhập số hàng của ma trận: "))
    cols = int(input("Nhập số cột của ma trận: "))
    matrix = generate_matrix(rows, cols)
    print(matrix)

    while True:
        print_menu()
        choice = input("Nhập lựa chọn của bạn (1-11): ")

        if choice == "1":
            print(calculate_determinant(matrix))

        elif choice == "2":
            print(find_inverse(matrix))

        elif choice == "3":
            print(sort_matrix_by_row(matrix))

        elif choice == "4":
            print(sort_matrix_by_column(matrix))

        elif choice == "5":
            print(sort_by_row_average(matrix))

        elif choice == "6":
            row = int(input("Nhập số hàng cần thay đổi: "))
            col = int(input("Nhập số cột cần thay đổi: "))
            new_value = int(input("Nhập giá trị mới: "))
            print(change_matrix_value(matrix, row, col, new_value))

        elif choice == "7":
            col_index = int(input("Nhập cột cần tăng giá trị lên 2: "))
            print(increase_column_value(matrix, col_index))

        elif choice == "8":
            vector = np.array([int(x) for x in input("Nhập vector (cách nhau bởi dấu cách): ").split()])
            print(add_vector_to_rows(matrix, vector))

        elif choice == "9":
            print(calculate_matrix_rank(matrix))

        elif choice == "10":
            U, S, V = calculate_svd(matrix)
            print("\nMatrix U:\n", U)
            print("\nSingular values (S):\n", S)
            print("\nMatrix V:\n", V)

        elif choice == "11":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()
