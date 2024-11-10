"""
CP1404/CP5632 Practical - Suggested Solution
Project Management Program.
Estimated time: 60 min (8:50)
Actual: 140 min
"""
from prac_07.project import Project
import datetime

VALID_CHOICES = "LSDFAUQ"
MENU = "- (L)oad projects\n" \
       "- (S)ave projects\n" \
       "- (D)isplay projects\n" \
       "- (F)ilter projects by date\n" \
       "- (A)dd new project\n" \
       "- (U)pdate project\n" \
       "- (Q)uit"


def main():
    projects = []
    load_projects_from_default_file(projects)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from projects.txt")
    print(MENU)

    choice = get_valid_choice()

    while choice != "Q":
        if choice == "D":
            display_projects(projects)

        elif choice == "U":
            update_project(projects)

        elif choice == "A":
            add_project(projects)

        elif choice == "F":
            filter_projects_by_date(projects)

        elif choice == "L":
            load_projects(projects)

        elif choice == "S":
            save_projects_to_file(projects)
        print(MENU)
        choice = get_valid_choice()
    print("Would you like to save to projects.txt? Y/n")
    save_projects_to_default_file(projects)
    print("Thank you for using custom-built project management software.")


def save_projects_to_default_file(projects):
    """Save projects to default file projects.txt"""
    if input(">>> ").upper() == "Y":
        with open("projects.txt", "w") as input_file:
            save_data_to_file(input_file, projects)


def save_data_to_file(input_file, projects):
    input_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
    for project in projects:
        input_file.write(f"{project.name}	"
                         f"{project.start_date.strftime('%d/%m/%Y')}	"
                         f"{project.priority}	"
                         f"{project.cost_estimate}	"
                         f"{project.completion_percentage}\n")


def save_projects_to_file(projects):
    """Save project list to user's file"""
    file_name = input("Enter filename: ")
    with open(file_name, "w") as input_file:
        save_data_to_file(input_file, projects)


def filter_projects_by_date(projects):
    """Show projects with start date after entered date"""
    while True:
        try:
            filter_date = datetime.datetime.strptime(
                input("Show projects that start after date (dd/mm/yyyy): "), "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date")
    for project in projects:
        if project.start_date > filter_date:
            print(project)


def load_projects_from_default_file(projects):
    """Load project list from default file projects.txt"""
    with open("projects.txt", "r") as in_file:
        next(in_file)
        for line in in_file:
            line = line.strip("\n").split("	")
            name = line[0]
            start_date = datetime.datetime.strptime(line[1], "%d/%m/%Y").date()
            priority = int(line[2])
            cost_estimate = float(line[3])
            completion_percentage = int(line[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
            projects.sort(key=lambda x: x.priority)


def load_projects(projects):
    """Load project list from user's file"""
    projects.clear()
    while True:
        try:
            file_name = input("Enter filename: ")
            with open(file_name, "r") as input_file:
                next(input_file)
                for line in input_file:
                    line = line.strip("\n").split("	")
                    name = line[0]
                    start_date = datetime.datetime.strptime(line[1], "%d/%m/%Y").date()
                    priority = int(line[2])
                    cost_estimate = float(line[3])
                    completion_percentage = int(line[4])
                    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
                    projects.sort(key=lambda x: x.priority)
                print(f"Loaded {len(projects)} projects from {file_name}")
                break
        except FileNotFoundError:
            print("Non-existing file")
        except OSError:
            print("Invalid file")


def update_project(projects):
    """Update status of existing project"""
    for i, project in enumerate(projects, 0):
        print(f"{i} " + str(project))
    while True:
        try:
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            break
        except ValueError:
            print("Invalid project number")
        except IndexError:
            print("Invalid project number")
    while True:
        try:
            percentage = input("New Percentage: ")
            if percentage == "":
                break
            percentage = int(percentage)
            if 0 <= percentage <= 100:
                projects[project_choice].completion_percentage = percentage
                break
            else:
                print("Number must be >= 0 and <= 100")
        except ValueError:
            print("Invalid input")
    while True:
        priority = input("New Priority: ")
        if priority == "":
            break
        try:
            priority = int(priority)
            if 0 < priority:
                projects[project_choice].priority = priority
                projects.sort(key=lambda x: x.priority)
                break
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input")


def add_project(projects):
    """Add new project to the list"""
    print("Let's add a new project")
    name = input("Name: ")
    while True:
        try:
            start_date = input("Start date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date")

    while True:
        try:
            priority = int(input("Priority: "))
            if 0 < priority:
                break
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input")

    while True:
        try:
            cost_estimate = int(input("Cost estimate: $"))
            if 0 <= cost_estimate:
                break
            else:
                print("Number must be >= 0")
        except ValueError:
            print("Invalid input")
    while True:
        try:
            percentage = int(input("Percent complete: "))
            if 0 <= percentage <= 100:
                break
            else:
                print("Number must be >= 0 and <= 100")
        except ValueError:
            print("Invalid input")
    projects.append(Project(name, start_date.strftime("%d/%m/%Y"), priority, cost_estimate, percentage))
    projects.sort(key=lambda x: x.priority)


def display_projects(projects):
    """Print list of loaded projects"""
    print("Incomplete projects: ")
    for i in projects:
        if i.completion_percentage != 100:
            start_date = i.start_date
            print(f"{i.name}, start: {start_date.strftime('%d/%m/%Y')}, priority {i.priority}, estimate: {i.cost_estimate}, "
                  f"completion:"
                  f" {i.completion_percentage}%")
    print("Complete projects: ")
    for i in projects:
        if i.completion_percentage == 100:
            print(f"{i.name}, start: {i.start_date.strftime('%d/%m/%Y')}, priority {i.priority}, estimate: {i.cost_estimate}, completion: {i.completion_percentage}%")



def get_valid_choice():
    """Get valid choice from user"""
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ")
    return choice.upper()


main()

