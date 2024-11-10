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



def get_valid_choice():
    """Get valid choice from user"""
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid choice")
        choice = input(">>> ")
    return choice.upper()


main()

