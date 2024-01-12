#Q)4)When processing data it is often useful to remove the last character from some input (it is often a newline).
# Write and test a function that takes a string parameter and returns it with the last character removed. 
# (If the string contains one or fewer characters, return it unchanged.)

def remove_last_character(input_string):
    return input_string[:-1] if len(input_string) > 1 else input_string

user_input = input("Enter a string: ")
result = remove_last_character(user_input)

print(f"Original string: {user_input}")
print(f"String with last character removed: {result}")
