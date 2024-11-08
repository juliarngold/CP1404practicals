from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')

        guitar = Guitar(parts[0], parts[1], parts[2])  # use parts of the lines in csv-file to create class objects
        guitars.append(guitar)  # append guitar object to list of guitars
        # print(guitar)
        print(guitars)
        print(type(guitar))
        # print(parts)
    in_file.close()
    # print(guitar_names)

#     sort_guitar_years()
#
#
#
# def sort_guitar_years(guitars):
#     for guitar in guitars:



# guitar =
# guitars.append(guitar)
#
# # Loop through and display all languages (using their str method)
# for guitar in guitars:
#     print(guitar)


main()
