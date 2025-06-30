try:
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    height = float(input("How tall are you in feet? "))

    birth_year = 2024 - age
    height_inches = height * 12
    name_length = len(name)

    print("Name: " + name)
    print("Age: " + str(age))
    print("Birth year: " + str(birth_year))
    print("Height in inches: " + str(height_inches))
    print("Your name has " + str(name_length) + " letters!")

except ValueError:
    print("Oops! Please enter numbers for age and height.")
