import os
from validation import is_valid_email, is_valid_phone

users = []
current_user = None
USERS_FILE = os.path.join("data", "users.txt")


def load_users():
    global users
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                first_name, last_name, email, password, phone = line.strip().split("|")
                users.append({
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "password": password,
                    "phone": phone
                })


def save_users():
    with open(USERS_FILE, "w") as f:
        for user in users:
            f.write(f"{user['first_name']}|{user['last_name']}|{user['email']}|{user['password']}|{user['phone']}\n")


def register_user():
    global users
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")

    if not is_valid_email(email):
        print("Invalid email! Must contain '@'.")
        return

    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    phone = input("Enter mobile phone: ")

    if not is_valid_phone(phone):
        print("Invalid phone number! Must start with '01' and be 11 digits.")
        return

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users.append(user)
    save_users()
    print("Registration successful!")


def login_user():
    global current_user
    email = input("Enter email: ")
    password = input("Enter password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            current_user = user
            print(f"Login successful! Welcome {user['first_name']}!")
            return
    print("Invalid email or password!")