import numpy as np

def generate_array():
    return np.random.randint(-100, 501, 10)

def output_all(array):
    print(f"Array: {array}")

def output_positions_2_5(array):
    print(f"Elements 2-5: {array[2:6]}")

def output_negative_values(array):
    neg_values = array[array < 0]
    print(f"Negative values: {neg_values}")

def output_range_x_y(array):
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    values = array[(array >= x) & (array <= y)]
    print(f"Values from {x} to {y}: {values}")

def filter_negative_values(array):
    array = array[array >= 0]
    print(f"Filtered Array: {array}")
    return array

def sort_ascending(array):
    array = np.sort(array)
    print(f"Sorted Ascending: {array}")
    return array

def sort_descending(array):
    array = np.sort(array)[::-1]
    print(f"Sorted Descending: {array}")
    return array

def output_statistics(array):
    stats = (
        f"Min: {np.min(array)}, Max: {np.max(array)}, Mean: {np.mean(array)}, "
        f"Median: {np.median(array)}, Std Dev: {np.std(array)}"
    )
    print(stats)

def delete_perfect_squares(array):
    array = array[~np.isin(array, [x ** 2 for x in range(int(np.sqrt(np.max(array))) + 1)])]
    print(f"Filtered Array (no squares): {array}")
    return array

def insert_value(array):
    x = int(input("Enter value to insert: "))
    v = int(input("Enter position: "))
    if 0 <= v <= len(array):
        array = np.insert(array, v, x)
    print(f"Array after insertion: {array}")
    return array


if __name__ == "__main__":
    arr = generate_array()
    while True:
        print("\nChoose an operation:")
        print("1. Output all values")
        print("2. Output elements with positions 2 to 5")
        print("3. Output negative values")
        print("4. Output elements within range X to Y")
        print("5. Filter out negative values")
        print("6. Sort ascending")
        print("7. Sort descending")
        print("8. Output statistics")
        print("9. Delete perfect squares")
        print("10. Insert value at position")
        print("11. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            output_all(arr)
        elif choice == "2":
            output_positions_2_5(arr)
        elif choice == "3":
            output_negative_values(arr)
        elif choice == "4":
            output_range_x_y(arr)
        elif choice == "5":
            arr = filter_negative_values(arr)
        elif choice == "6":
            arr = sort_ascending(arr)
        elif choice == "7":
            arr = sort_descending(arr)
        elif choice == "8":
            output_statistics(arr)
        elif choice == "9":
            arr = delete_perfect_squares(arr)
        elif choice == "10":
            arr = insert_value(arr)
        elif choice == "11":
            break
        else:
            print("Invalid choice, try again.")
