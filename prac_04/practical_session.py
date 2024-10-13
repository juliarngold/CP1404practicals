


names = ["Ada", "Alan", "Bill", "John"]
print(",".join(names))
name_to_remove = input("What do you want to remove? ")
while len(names) != 0:
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Please try again.")
    print(names)
    name_to_remove = input("What do you want to remove? ")

