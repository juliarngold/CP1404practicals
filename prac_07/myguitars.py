from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = parts[0]  # store only the guitar name
        guitars.append(guitar)
    in_file.close()
    print(guitars)

    # guitar =
    # guitars.append(guitar)
    #
    # # Loop through and display all languages (using their str method)
    # for guitar in guitars:
    #     print(guitar)


main()
