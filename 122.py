import numpy as np

def gauss_elimination(A, B):
    """
    Solve the system of equations Ax = B using Gauss method
    Input:
    - A: coefficient matrix (numpy array)
    - B: right column vector (numpy array)
    Output:
    - x: vector of solutions of a system of equations (numpy array)
    """
    n = len(B)
    # Append matrix B to A to form an expanded matrix
    AB = np.column_stack((A, B))
    # Apply Gauss method to transform matrix AB into upper triangular matrix
    for i in range(n):
    # Find the row containing the largest element in column i and transpose it to the top of the column
        max_row = np.argmax(np.abs(AB[i:, i])) + i
        AB[[i, max_row]] = AB[[max_row, i]]
    # Loop through the rows below to remove elements in column i
    for j in range(i + 1, n):
        ratio = AB[j, i] / AB[i, i]
        AB[j, :] -= ratio * AB[i, :]
    # Calculate the solution of the system of equations by the back method
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (AB[i, -1] - np.dot(AB[i, :-1], x)) / AB[i, i]
        return x

# Usage example:
A = np.array([[2, 3, 1],
 [4, 7, 5],
 [2, 5, 2]], dtype=float)
B = np.array([5, 10, 6], dtype=float)
x = gauss_elimination(A, B)
print("The solution of the system of equations is:", x)