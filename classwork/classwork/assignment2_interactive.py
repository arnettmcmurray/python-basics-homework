name = input("What's your name? ")
fav_number = int(input("What's your favorite number? "))
birth_year = int(input("What year were you born? "))

from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year
turns_100 = birth_year + 100
days_alive = age * 365
fav_number_squared = fav_number ** 2

print(f"\n=== {name}'s Profile ===")
print(f"Age: {age} years old")
print(f"You'll turn 100 in the year {turns_100}!")
print(f"Your favorite number squared is {fav_number_squared}!")
print(f"Fun fact: You've been alive for roughly {days_alive:,} days!")
