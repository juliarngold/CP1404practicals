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

