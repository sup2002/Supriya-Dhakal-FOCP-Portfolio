#Q)2)Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively:
#Letters that appear in at least one of the two words.
#Letters that appear in both words.
#Letters that appear in either word, but not in both.
#Hint: These could all be done programmatically, but consider carefully what topic we have been discussing this week! Each function can be exactly one line

import string

def letters_in_either_from_user():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    return sorted(set(word1.lower() + word2.lower()))

def letters_in_both_from_user():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    return sorted(set(char.lower() for char in word1 if char.isalpha()) & set(char.lower() for char in word2 if char.isalpha()))

def letters_in_either_not_both_from_user():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    return sorted((set(char.lower() for char in word1 if char.isalpha()) ^ set(char.lower() for char in word2 if char.isalpha())))

result1 = letters_in_either_from_user()
print(f"Letters in either word: {result1}")

result2 = letters_in_both_from_user()
print(f"Letters in both words: {result2}")

result3 = letters_in_either_not_both_from_user()
print(f"Letters in either word, but not in both: {result3}")
