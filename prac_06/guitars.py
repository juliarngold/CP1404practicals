"""
Estimated time: 20 min
Actual time: 25 min
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = get_valid_year()
        cost = get_valid_cost()
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    print("These are my guitars:")
    print_guitars(guitars)


def print_guitars(guitars):
    """Display collection of guitars"""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def get_valid_cost():
    """Get valid guitar's cost"""
    while True:
        try:
            cost = float(input("Cost: $"))
            break
        except ValueError:
            print("Invalid cost")
            pass
    return cost


def get_valid_year():
    """Get valid guitar's year"""
    while True:
        try:
            year = float(input("Year: "))
            break
        except ValueError:
            print("Invalid year")
            pass
    return year


main()