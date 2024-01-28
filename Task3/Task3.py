import codecs
import getpass

# Function to encrypt the password using ROT-13
def encrypt_password(password):
    return codecs.encode(password, 'rot_13')

# Function to read the password file and return the lines as a list
def read_password_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Function to write the lines to the password file
def write_password_file(filename, lines):
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

# Function to add a new user to the password file
def add_user(filename):
    # Get user input
    new_username = input("Enter new username: ").strip()
    real_name = input("Enter real name: ").strip()
    new_password = encrypt_password(getpass.getpass("Enter password: ").strip())

    lines = read_password_file(filename)

    # Check if the username already exists
    for line in lines:
        if line.startswith(new_username + ":"):
            print("Cannot add. Most likely username already exists.")
            return

    new_entry = f"{new_username}:{real_name}:{new_password}"
    lines.append(new_entry)
    write_password_file(filename, lines)

    print("User created.")

# Function to delete a user from the password file
def delete_user(filename):
    # Get user input
    username_to_delete = input("Enter username: ").strip()

    lines = read_password_file(filename)

    # Find and delete the user if it exists
    for i, line in enumerate(lines):
        if line.startswith(username_to_delete + ":"):
            del lines[i]
            write_password_file(filename, lines)
            print("User deleted.")
            return

    print("User not found. Nothing changed.")

# Function to change a user's password in the password file
def change_password(filename):
    # Get user input
    username_to_change = input("User: ").strip()
    current_password = encrypt_password(getpass.getpass("Current Password: ").strip())
    new_password = encrypt_password(getpass.getpass("New Password: ").strip())
    confirm_password = encrypt_password(getpass.getpass("Confirm: ").strip())

    lines = read_password_file(filename)

    # Find the user and change the password if conditions are met
    for i, line in enumerate(lines):
        if line.startswith(username_to_change + ":"):
            stored_password = line.split(":")[2]

            if current_password == stored_password:
                if new_password == confirm_password:
                    lines[i] = f"{username_to_change}:{line.split(':')[1]}:{new_password}"
                    write_password_file(filename, lines)
                    print("Password changed.")
                else:
                    print("Passwords do not match. Nothing changed.")
            else:
                print("Current password is invalid. Nothing changed.")

            return

    print("User not found. Nothing changed.")

# Function to perform user login
def login(filename):
    # Get user input
    username_to_login = input("User: ").strip()
    password_to_login = encrypt_password(getpass.getpass("Password: ").strip())

    lines = read_password_file(filename)

    # Check if the username and password match in the password file
    for line in lines:
        if line.startswith(username_to_login + ":"):
            stored_password = line.split(":")[2]

            if password_to_login == stored_password:
                print("Access granted.")
            else:
                print("Access denied.")

            return

    print("User not found. Access denied.")

if __name__ == "__main__":
    filename = "passwd.txt"

    while True:
        print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
        choice = input("Select an option (1-5): ")

        # Menu for user interaction
        if choice == '1':
            add_user(filename)
        elif choice == '2':
            delete_user(filename)
        elif choice == '3':
            change_password(filename)
        elif choice == '4':
            login(filename)
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
