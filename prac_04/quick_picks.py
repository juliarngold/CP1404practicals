"""
CP1404/CP5632 Practical
Do-from-scratch Exercises
"Quick Pick" Lottery Ticket Generator
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6

numbers = []
number_of_picks = int(input("How many quick picks? "))
while number_of_picks < 0:
    print("Invalid input")
    number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    quick_pick = []
    numbers.append(random.randint(1, 45))
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))







