def calculate_average_and_level(scores):
    average = sum(scores) / len(scores)
    if average < 5:
        level = "Weak"
    elif average < 7:
        level = "Pass"
    elif average < 8:
        level = "Strong Pass"
    elif average < 9:
        level = "Good"
    else:
        level = "Excellent"
    return average, level

while True:
    try:
        score = list(map(float, input("Enter your scores (0.0 to 10.0): ").split()))
        if not all(0 <= x <= 10 for x in score):
            print("Scores must be between 0.0 and 10.0. Please try again.")
            continue

        average, level = calculate_average_and_level(score)
        print(f"Average Score: {average:.2f}")
        print(f"Level: {level}")

        another = input("Do you want to enter another set of scores? (y/n): ").strip().lower()
        if another != "y":
            break
    except ValueError:
        print("Invalid input. Please enter numeric values.")
