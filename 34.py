res =[]

a = int(input("Nhap so phan tu trong mang: "))
for i in range(a):
    b = int(input(f"Nhap phan tu thu {i} trong mang: "))
    res.append(b)

def list_odd_numbers(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            count += 1
            print(i,end=' ')
    print('')
    print(f"Number of odd numbers: {count}")

def list_even_numbers(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
            print(i,end=' ')
    print('')
    print(f"Number of even numbers: {count}")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(arr):
    print('Prime Numbers: ',end='')
    for i in arr:
        if is_prime(i):
            print(i,end=' ')
    print('')

def non_prime_numbers(arr):
    print('Non-Prime Numbers: ', end='')
    for i in arr:
        if not is_prime(i):
            print(i, end=' ')
    print('')

def remove_even_numbers(arr):
    rv_even_numbers = [x for x in arr if x % 2 != 0]
    print(f"Remove even numbers: {rv_even_numbers}")

list_odd_numbers(res)
list_even_numbers(res)
prime_numbers(res)
non_prime_numbers(res)
remove_even_numbers(res)



