"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print(convert_celsius_into_fahrenheit(float(input("Celsius: "))))
        elif choice == "F":
            print(convert_fahrenheit_into_celsius(float(input("Fahrenheit: "))))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_into_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"{celsius:.2f}"


def convert_celsius_into_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"{fahrenheit:.2f}"


main()
