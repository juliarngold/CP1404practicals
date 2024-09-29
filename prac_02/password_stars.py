"""
CP1404/CP5632 - Practical
Refactoring- Password Check with Functions
"""

MINIMUM_LENGTH= 4
password= input("Enter a password: ")
while len(password) < MINIMUM_LENGTH:
    print("Invalid password")
    password = input("Enter a password: ")
for i in range(len(password)):
    print("*", end="")
