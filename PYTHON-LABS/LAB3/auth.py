import os
from validation import is_valid_email, is_valid_phone

users = []
current_user = None
USERS_FILE = os.path.join("data", "users.txt")


def get_current_user():
    return current_user


def load_users():
    global users
    os.makedirs("data", exist_ok=True)  # Create data folder if it doesn't exist
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split("|")
                    if len(parts) == 5:  # Make sure we have all parts
                        first_name, last_name, email, password, phone = parts
                        users.append({
                            "first_name": first_name,
                            "last_name": last_name,
                            "email": email,
                            "password": password,
                            "phone": phone
                        })


def save_users():
    os.makedirs("data", exist_ok=True)  # Create data folder if it doesn't exist
    with open(USERS_FILE, "w") as f:
        for user in users:
            f.write(f"{user['first_name']}|{user['last_name']}|{user['email']}|{user['password']}|{user['phone']}\n")


def register_user():
    global users
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")

    # Check if email already exists
    for user in users:
        if user["email"] == email:
            print("Email already exists! Please use a different email.")
            return

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
            return user  # Return the user object
    
    print("Invalid email or password!")
    return None


def logout_user():
    global current_user
    if current_user:
        print(f"Goodbye {current_user['first_name']}!")
        current_user = None
    else:
        print("No user is currently logged in.")


def is_logged_in():
    return current_user is not None