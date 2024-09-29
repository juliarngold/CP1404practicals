"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    while 0 <= score <= 100:
        message = determine_result(score)
        print(message)
        score = float(input("Enter score: "))
    print("Invalid score")


def determine_result(score):
    if score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message
