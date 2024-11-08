from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])  # use parts of the lines in csv-file to create class objects
        guitars.append(guitar)  # append guitar object to list of guitars
    in_file.close()
    display_guitars_sorted_by_year(guitars)
    add_new_guitar_to_list(guitars)


def add_new_guitar_to_list(guitars):
    print("Let's add a new guitar")
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ", "Invalid year", int)
        cost = get_valid_number("Cost: $", "Invalid cost", float)
        guitars.append(Guitar(name, year, cost))  # add new guitar to guitar list
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")


def display_guitars_sorted_by_year(guitars):
    """display guitars sorted by their year"""
    guitars.sort()  # sort guitars by year
    for guitar in guitars:
        print(guitar)


def get_valid_number(prompt, message, data_type):
    """Get valid guitar number for guitar's year and cost"""
    while True:
        try:
            number = data_type(input(prompt))
            break
        except ValueError:
            print(message)
            pass
    return number




main()
