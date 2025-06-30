history = []

while True:
    print("\n=== Mini Calculator ===")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Quit")

    choice = input("Choose operation (1-6): ")

    if choice == "6":
        print("Goodbye!")
        break

    if choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid option.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = num1 + num2
        symbol = "+"
    elif choice == "2":
        result = num1 - num2
        symbol = "-"
    elif choice == "3":
        result = num1 * num2
        symbol = "*"
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            continue
        result = num1 / num2
        symbol = "/"
    elif choice == "5":
        result = num1 ** num2
        symbol = "^"

    output = f"Result: {num1} {symbol} {num2} = {result}"
    history.append(output)
    print(output)

print("\n--- Calculation History ---")
for entry in history:
    print(entry)
