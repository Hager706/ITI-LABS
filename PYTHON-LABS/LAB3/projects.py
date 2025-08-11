import os
from auth import get_current_user, users
from validation import is_valid_number

projects = []
PROJECTS_FILE = os.path.join("data", "projects.txt")


def load_projects():
   
    global projects
    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, "r") as f:
            for line in f:
                title, details, target, start_date, end_date, owner_email = line.strip().split("|")
                projects.append({
                    "title": title,
                    "details": details,
                    "target": target,
                    "start_date": start_date,
                    "end_date": end_date,
                    "owner_email": owner_email
                })


def save_projects():
    with open(PROJECTS_FILE, "w") as f:
        for p in projects:
            f.write(f"{p['title']}|{p['details']}|{p['target']}|{p['start_date']}|{p['end_date']}|{p['owner_email']}\n")


def create_project():
    current_user = get_current_user()
    if current_user is None:
        print("Please login first!")
        return

    title = input("Enter project title: ")
    details = input("Enter project details: ")
    target = input("Enter total target (EGP): ")

    if not is_valid_number(target):
        print("Target must be a number!")
        return

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    project = {
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
        "owner_email": current_user["email"]
    }

    projects.append(project)
    save_projects()
    print("Project created successfully!")


def view_all_projects():
    if not projects:
        print("No projects available.")
        return

    for i, p in enumerate(projects, start=1):
        print(f"Project #{i}: {p['title']}")
        print(f"Details: {p['details']}")
        print(f"Target: {p['target']} EGP")
        print(f"Owner: {p['owner_email']}")
        print(f"Duration: {p['start_date']} to {p['end_date']}")
        print("---")


def view_my_projects():
    current_user = get_current_user()
    if current_user is None:
        print("Please login first!")
        return

    my_projects = [p for p in projects if p["owner_email"] == current_user["email"]]

    if not my_projects:
        print("You have no projects.")
        return

    for i, p in enumerate(my_projects, start=1):
        print(f"Project #{i}: {p['title']}")
        print(f"Details: {p['details']}")
        print(f"Target: {p['target']} EGP")
        print(f"Duration: {p['start_date']} to {p['end_date']}")
        print("---")


def edit_project():
    current_user = get_current_user()
    if current_user is None:
        print("Please login first!")
        return

    my_projects = [p for p in projects if p["owner_email"] == current_user["email"]]

    if not my_projects:
        print("You have no projects to edit.")
        return

    for i, p in enumerate(my_projects, start=1):
        print(f"{i}. {p['title']}")

    try:
        choice = int(input("Enter the number of the project to edit: "))
        if choice < 1 or choice > len(my_projects):
            print("Invalid choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    project_to_edit = my_projects[choice - 1]

    project_to_edit["title"] = input("Enter new title: ")
    project_to_edit["details"] = input("Enter new details: ")
    target = input("Enter new target (EGP): ")
    if not is_valid_number(target):
        print("Target must be a number!")
        return
    project_to_edit["target"] = target
    project_to_edit["start_date"] = input("Enter new start date (YYYY-MM-DD): ")
    project_to_edit["end_date"] = input("Enter new end date (YYYY-MM-DD): ")

    save_projects()
    print("Project updated successfully!")


def delete_project():
    current_user = get_current_user()
    if current_user is None:
        print("Please login first!")
        return

    my_projects = [p for p in projects if p["owner_email"] == current_user["email"]]

    if not my_projects:
        print("You have no projects to delete.")
        return

    for i, p in enumerate(my_projects, start=1):
        print(f"{i}. {p['title']}")

    try:
        choice = int(input("Enter the number of the project to delete: "))
        if choice < 1 or choice > len(my_projects):
            print("Invalid choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    project_to_delete = my_projects[choice - 1]
    projects.remove(project_to_delete)
    save_projects()
    print("Project deleted successfully!")