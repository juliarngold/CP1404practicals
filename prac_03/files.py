"""
CP1404/CP5632 - Practical
Files- Do from scratch
"""

"""ask the user for their name, open a file called name.txt and write that name to it"""
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

"""open "name.txt" and read the name (as above) then print"""
in_file = open(FILENAME, 'r')
name_from_file = in_file.readline().strip()  # Read the name
in_file.close()
print(f"Hi {name_from_file}!")

"""open numbers.txt, read only the first two numbers, add them together then print the result"""
with open('numbers.txt', 'r') as file:
    total = 0
    for i in range(2):  # for the first two lines
        number = int(file.readline().strip())  # convert each line to an integer
        total += number  # add first two numbers together
    print(total)

"""print the total for all lines"""
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())  # Sum all numbers
    print(total)  # Prints the total of all numbers in the file

