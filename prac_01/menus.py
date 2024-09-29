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

MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")
print(MENU)
users_choice = input(">>> ").upper()
while users_choice != "Q":
    if users_choice == "H":
        print(f'Hello {name}')
    elif users_choice == "G":
        print(f'Goodbye {name}')
    else:
        print("Invalid choice")
    print(MENU)
    users_choice = input(">>> ").upper()
print("Finished.")