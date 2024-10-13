FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    """Read data from the file"""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display data"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
