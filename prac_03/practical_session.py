# # REWRITE THE FOLLOWING
# name = input("What is your name? ")
# out_file = open("my_name.txt", "w")
# print(name, file=out_file)
# out_file.close()
# print("Done")
#
# # with open doesn't require to close
# filename = input("Enter filename ")
# with open("filename", "r") as out_file:
#     print()
# print("done")
#
# """write a code that created files from a list of strings. Each file should be named with the value of the string
# extension. If the string is "BOB" create a file called "BOB". Write the string to the file"""
# names = ['Kyle', 'James', 'Anna']
# for name in names:
#     out_file = open(f"{name}.txt", "w")  # created a file for each name, here openwith also can
#     print(name, file=out_file)  # prints the name inside the file
#     out_file.close()
#
# """Write the position in the list to the file, starting from 1 """
# print("????")

"""Write code to read a file like this and print each data pair like, "Bob was born in NZ". """
FILENAME = "countries.txt"
in_file = open(FILENAME, "r")
for line in in_file:
    name = line.strip()
    country = in_file.readline().strip()
    print(f"{name} was born in {country}.")
in_file.close()


