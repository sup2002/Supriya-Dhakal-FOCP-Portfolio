#Q)2)Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string. 
# Test the function with a short program.

def count_case(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return uppercase_count, lowercase_count

input_string = input("Enter a string: ")
upper, lower = count_case(input_string)

print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")

