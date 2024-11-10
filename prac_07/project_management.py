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

