#Q)3)Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.

password1 = input("Enter a new password (8-12 characters): ")

if 8 <= len(password1) <= 12 and password1 == input("Enter the password again: "):
    print("Password Set")
else:
    print("Error: Password does not meet the length constraint or passwords do not match.")
