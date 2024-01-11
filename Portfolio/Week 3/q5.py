#Q)5)Modify your program a final time so that it executes until the user successfully chooses a password. That is, if the password chosen fails any of the checks, the program should return to asking for the password the first time.

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8-12 characters): ")
    
    if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS and password1 == input("Enter the password again: "):
        print("Password Set")
        break
    else:
        print("Error: Password does not meet the constraints. Please try again.")

