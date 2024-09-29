"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

import random

VALID_MINIMAL_SCORE_THRESHOLD = 0
VALID_MAXIMUM_SCORE_THRESHOLD = 100
EXCELLENT_SCORE_THRESHOLD = 90
BAD_SCORE_THRESHOLD = 50


def main():
    """determine and display score status"""
    score = float(input("Enter score: "))
    print(determine_score(score))
    print(determine_score(random.randint(0, 100)))


def determine_score(score):
    """determine score status"""
    if score < VALID_MINIMAL_SCORE_THRESHOLD or score > VALID_MAXIMUM_SCORE_THRESHOLD:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE_THRESHOLD:
        return "Excellent"
    elif score >= BAD_SCORE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
