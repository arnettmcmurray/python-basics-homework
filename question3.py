def calculate_average(scores):
    return sum(scores) / len(scores)

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        count = int(input("How many test scores do you want to enter? "))
    except ValueError:
        print("Invalid number.")
        return

    scores = []
    i = 1
    while i <= count:
        try:
            score = float(input(f"Enter score {i}: "))
            scores.append(score)
            i += 1
        except ValueError:
            print("Please enter a valid number.")

    average = calculate_average(scores)
    grade = get_letter_grade(average)

    print("\n=== GRADE REPORT ===")
    print(f"Test Scores: {scores}")
    print(f"Average Score: {average:.2f}")
    print(f"Letter Grade: {grade}")

main()