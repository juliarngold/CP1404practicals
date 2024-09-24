"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while 0 <= score <= 100:
    if score >= 90:
        message= "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    print(message)
    score = float(input("Enter score: "))
print("Invalid score")
