"""
CP1404/CP5632 - Practical
Menu


display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""

MINIMAL_SCORE_THRESHOLD = 0
MAXIMUM_SCORE_THRESHOLD = 100
EXCELLENT_SCORE_THRESHOLD = 90
BAD_SCORE_THRESHOLD = 50
VALID_CHOICES = "gpsq"
VALID_HIGH_THRESHOLD = 100
VALID_LOW_THRESHOLD = 0
DEFAULT_SCORE = 0
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Display a menu that allows the user to get a valid score, print a result, show asterisks, or quit."""
    score = DEFAULT_SCORE
    print(MENU)
    choice = get_valid_choice()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            print(determine_score(score))
        elif choice == "s":
            print_asterisks(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = get_valid_choice()
    print("Farewell")


def get_valid_choice():
    """get valid input for menu choice"""
    choice = input(">>> ").lower()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ")
    return choice


def get_valid_score():
    """get valid score"""
    score = int(input("Enter score: "))
    while score < VALID_LOW_THRESHOLD or score > VALID_HIGH_THRESHOLD:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_asterisks(length):
    """display asterisks"""
    print("*" * length)


def determine_score(score):
    """determine status of score"""
    if score >= EXCELLENT_SCORE_THRESHOLD:
        return "Excellent"
    elif score >= BAD_SCORE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
