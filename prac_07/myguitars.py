from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])  # use parts of the lines in csv-file to create class objects
        guitars.append(guitar)  # append guitar object to list of guitars
    in_file.close()

    guitars.sort()  # sort guitars by year
    for guitar in guitars:
        print(guitar)


main()
