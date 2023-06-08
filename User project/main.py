from Menunode import generate_menu_from_dict
from Userclass import *
from contacts import *
from Utils import get_input
from action import *

manager_menu_route = {
    "name": "User page",
    "children": [
        {
            "name": "Add a new contacts",
            "action": add_contacts,
        },
        {
            "name": "Edit contacts",
            "action": edit_contacts,
        },
        {
            "name": "View all contacts",
            "action": view_all_contacts,
        },
        {
            "name": "View categorie",
            "action": category,
        },
        {
            "name": "Delete a contact",
            "action": delete_contact,
        },
        {
            "name": "Search contact",
            "children": [
                {
                    "name": "search by name",
                    "action": search_nam,
                },
                {
                    "name": "search by email",
                    "action": search_mail,
                },
                {
                    "name": "search by phone",
                    "action": search_phon,
                },
            ],
        },
        {
            "name": "export csv file",
            "action": csv_file,
        
        },
        {
            "name": "Exit",
            "action": page_exit,
        },
    ],
}
    


root_menu = generate_menu_from_dict(manager_menu_route)
# root_menu()

def main():
    print()
    while True:
        choose=int(input("Login (1)\nSign-up (2)\nExit (3)\n"))
        if choose == 1:
            username = get_input("Username: ")
            password = get_input("Password: ")

            #try:
            login =User.login(username, password)
            if login:
                print(f"Welcome {username}\n")
                root_menu()
            else:
                main()
            #except Exception as e:
                #print(e)
            

        elif choose==2:
            username = get_input("Username: ")
            password = get_input("Password: ")
            try:
                sign_up = User.register(username, password)
                if sign_up:
                    print(f"Welcome {username}\n")
                    sign_up.save_file()
                    root_menu()
                else:
                    main()
            except Exception as e:
                print(e)
        elif choose==3:
            exit()
        else:
            print("Please choose correct number\n")
main()