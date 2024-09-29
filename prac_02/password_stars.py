"""
CP1404/CP5632 - Practical
Refactoring- Password Check with Functions
"""


def main():
    password = get_password(4)
    display_password(password)


def display_password(password):
    for i in range(len(password)):
        print("*", end="")


def get_password(minimum_length):
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input("Enter a password: ")
    return password


main()
