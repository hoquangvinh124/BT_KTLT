def output_digit(nums):
    print("\n".join(map(str, split_value(nums))))

def split_value(nums):
    arr = nums.split(";")
    return list(map(int, arr))

def even_digit_statics(nums):
    nums = split_value(nums)
    new_arr = [x for x in nums if x % 2 == 0]
    print("\n", new_arr)
    print(f"Even digit: {len(new_arr)}")

def negative_digit_statics(nums):
    nums = split_value(nums)
    new_arr = [x for x in nums if x < 0]
    print("\n", new_arr)
    print(f"Negative digit: {len(new_arr)}")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_digit_statics(nums):
    nums = split_value(nums)
    new_arr = [x for x in nums if is_prime(x)]
    print("\n", new_arr)
    print(f"Prime digit: {len(new_arr)}")

def average_value(nums):
    nums = split_value(nums)
    total = sum(nums)
    print(f"\nAverage value: {total / len(nums)}")

example = input("Enter string split by ; ")

output_digit(example)
even_digit_statics(example)
negative_digit_statics(example)
prime_digit_statics(example)
average_value(example)

