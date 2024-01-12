#Q)1)Functions are often used to validate input. Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise.
# Write a short program to test the function.

def is_in_range(number):
    return 0 <= number <= 100
user_input = int(input("Enter an integer: "))
print(f"{user_input} is {'in' if is_in_range(user_input) else 'outside'} the range 0 to 100.")
