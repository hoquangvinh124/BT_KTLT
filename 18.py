import math

def fibonacci_formula(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    fib_n = (phi**n - psi**n) / sqrt_5
    return round(fib_n)

def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def list_fibonacci(n):
    for i in range(1,n+1):
        print(fibonacci_recursive(i),end='\t')

def fibonacci_iterative(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

print(fibonacci_formula(9))
print(fibonacci_recursive(9))
print(fibonacci_iterative(9))
list_fibonacci(9)

