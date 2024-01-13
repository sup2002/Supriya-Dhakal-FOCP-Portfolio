#Q)1)Write and test a function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string. 
# So, if the string is cheese, the list returned should be ['c', 'e', 'h', 's'].

def unique_letters_sorted(input_string):
    return sorted(set(char.lower() for char in input_string if char.isalpha()))

input_str = "cheese"
result = unique_letters_sorted(input_str)
print(f"Original String: {input_str}")
print(f"Unique Letters Sorted: {result}")
