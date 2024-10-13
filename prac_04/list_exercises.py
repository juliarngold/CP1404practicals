"""
CP1404/CP5632 Practical
Basic list operations
"""
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    while number < 0:
        print("Invalid input")
        number = int(input("Enter a number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


""" Ask the user for their username. If the username is in the above list of authorised users, 
print "Access granted", otherwise print "Access denied" """
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your name: ")
if username in usernames:
    message = "Access granted"
else:
    message = "Access denied"
print(message)
