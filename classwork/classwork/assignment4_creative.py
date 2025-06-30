import random

name = input("Enter a character name: ")
setting = input("Enter a setting (e.g., jungle, spaceship): ")
action = input("Enter an action (e.g., dancing, fighting): ")

twists = [
    "an alien invasion started",
    "a treasure map appeared",
    "gravity turned off suddenly",
    "they found a talking animal",
    "the lights went out mysteriously"
]

twist = random.choice(twists)

print(f"""
=== {name}'s {setting.capitalize()} Adventure ===
{name} was deep in the {setting} when suddenly...
they started {action}! Just then, {twist}!

Nobody saw it coming, but it changed everything.

The end.
""")
