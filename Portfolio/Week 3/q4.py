#Q)4)Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus:
#BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter a new password (8-12 characters): ")

if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS and password1 == input("Enter the password again: "):
    print("Password Set")
else:
    print("Error: Password does not meet the constraints.")
