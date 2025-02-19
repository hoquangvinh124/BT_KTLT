import numpy as np

def get_matrix_dimensions(name):
    print(f"Enter dimensions for {name}:")
    N = int(input("Number of rows: "))
    M = int(input("Number of columns: "))
    return N, M

def create_random_matrix(N, M, low=-100, high=101):
    return np.random.randint(low, high, (N, M))

def matrix_sum(A, B):
    if A.shape == B.shape:
        return A + B
    return None

def matrix_difference(A, B):
    if A.shape == B.shape:
        return A - B
    return None

def matrix_multiplication(A, B):
    if A.shape[1] == B.shape[0]:
        return A.dot(B)
    return None

def hadamard_product(A, B):
    if A.shape == B.shape:
        return A * B
    return None

def solve_linear_equation(A, B):
    if A.shape[0] == A.shape[1] and B.shape[0] == A.shape[0] and B.shape[1] == 1:
        try:
            x = np.linalg.solve(A, B)
            return x
        except ValueError:
            return None
    return None

def main():
    N1, M1 = get_matrix_dimensions("Matrix A")
    N2, M2 = get_matrix_dimensions("Matrix B")
    A = create_random_matrix(N1, M1)
    B = create_random_matrix(N2, M2)

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    sum_ab = matrix_sum(A, B)
    if sum_ab is not None:
        print("\nSum of A and B:")
        print(sum_ab)
    else:
        print("\nCannot add A and B")

    diff_ab = matrix_difference(A, B)
    if diff_ab is not None:
        print("\nDifference of A and B:")
        print(diff_ab)
    else:
        print("\nCannot subtract A and B")

    product_ab = matrix_multiplication(A, B)
    if product_ab is not None:
        print("\nMatrix product (A x B):")
        print(product_ab)
    else:
        print("\nCannot multiply A and B")

    hadamard_ab = hadamard_product(A, B)
    if hadamard_ab is not None:
        print("\nHadamard product of A and B:")
        print(hadamard_ab)
    else:
        print("\nCannot perform Hadamard product")

    if N1 == M1 and N2 == N1 and M2 == 1:
        solution = solve_linear_equation(A, B)
        if solution is not None:
            print("\nSolution to A * x = B:")
            print(solution)
        else:
            print("\nCannot solve the system A * x = B")
    else:
        print("\nCannot solve A * x = B with the given dimensions")

main()