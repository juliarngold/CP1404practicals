"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? If the numerator or denominator are not integers
2. When will a ZeroDivisionError occur? when the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_input = False
try:
    numerator = int(input("Enter the numerator: "))

    while not valid_input:  # while true
        try:
            denominator = int(input("Enter the denominator: "))
            fraction = numerator / denominator
            print(fraction)
            valid_input = True  # set to True to exit the loop once valid input is received
        except ZeroDivisionError:  # if denominator equals to zero
            print("Cannot divide by zero!")

except ValueError:  # if not integers
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
