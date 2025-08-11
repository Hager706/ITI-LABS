import auth
from auth import register_user, login_user, get_current_user, load_users
from projects import create_project, view_all_projects, view_my_projects, edit_project, delete_project, load_projects

load_users()
load_projects()


def show_main_menu():
    current_user = get_current_user()  
    if current_user:
        print(f"\nLogged in as: {current_user['first_name']}")
    choice = input("""Crowdfunding App 
1. Register
2. Login
3. View All Projects
4. Create Project
5. View My Projects
6. Edit My Project
7. Delete My Project
8. Exit
Choose an option (1-8): """)
    return choice


while True:
    menu = show_main_menu()

    if menu == "1":
        register_user()
    elif menu == "2":
        current_user = get_current_user()
        if current_user:
          print("You are already logged in!")
        else:
          login_user()
    elif menu == "3":
        view_all_projects()
    elif menu == "4":
        create_project()
    elif menu == "5":
        view_my_projects()
    elif menu == "6":
        edit_project()
    elif menu == "7":
        delete_project()
    elif menu == "8":
        print("Exit")
        break
    else:
        print("Invalid input")