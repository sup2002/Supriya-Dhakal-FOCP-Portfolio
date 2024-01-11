#Q)1)Modify your greeting program so that if the user does not enter a name (i.e. they just press enter), the program responds "Hello, Stranger!".
# Otherwise it should print a greeting with their name as before

user_name = input("Hello, what is your name? ")

if user_name:
    print(f"Hello, {user_name}. Good to meet you!")
else:
    print("Hello, Stranger!")
