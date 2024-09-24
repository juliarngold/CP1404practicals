"""
CP1404/CP5632 - Practical
5. Menus

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU_CHOICE_H = "(H)ello"
MENU_CHOICE_G = "(G)oodbye"
MENU_CHOICE_Q = "(Q)uit"
name = input("Enter name: ")
print(MENU_CHOICE_H)
print(MENU_CHOICE_G)
print(MENU_CHOICE_Q)
users_choice = input(">>> ").upper()
while users_choice != "Q":
    if users_choice == "H":
        print(f'Hello {name}')
    elif users_choice == "G":
        print(f'Goodbye {name}')
    else:
        print("Invalid choice")
    print(MENU_CHOICE_H)
    print(MENU_CHOICE_G)
    print(MENU_CHOICE_Q)
    users_choice = input(">>> ").upper()
print("Finished.")