"""
CP1404/CP5632 - Practical
Refactoring- Password Check with Functions
"""


def main():
    """check and display password"""
    password = get_password(4)
    display_password(password)


def display_password(password):
    """print password as asteriks"""
    for i in range(len(password)):
        print("*", end="")


def get_password(minimum_length):
    """check password for required length"""
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input("Enter a password: ")
    return password


main()

