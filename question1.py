def calculate_budget():
    print("=== PERSONAL BUDGET CALCULATOR ===")

    try:
        income = float(input("Enter your monthly income: $"))
        rent = float(input("Enter rent expense: $"))
        food = float(input("Enter food expense: $"))
        entertainment = float(input("Enter entertainment expense: $"))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    total_expenses = rent + food + entertainment
    remaining = income - total_expenses

    print("\n=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money: ${remaining:.2f}")

    if remaining < 0:
        print("\nBudget Advice: You're overspending! Cut back on expenses.")
    elif remaining < 100:
        print("\nBudget Advice: Your budget is tight. Be careful with spending.")
    else:
        print("\nBudget Advice: Great job! You have money left over.")

calculate_budget()