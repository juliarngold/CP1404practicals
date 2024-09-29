"""
CP1404/CP5632 - Practical
Refactoring- Password Check with Functions
"""
MINIMUM_LENGTH= 4
def main():
    password = get_password()
    display_password(password)


def display_password(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter a password: ")
    return password


main()
