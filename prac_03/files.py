"""
CP1404/CP5632 - Practical
Files- Do from scratch
"""

FILENAME = "name.txt"
out_file= open(FILENAME, 'w')
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()
