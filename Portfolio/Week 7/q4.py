#Q)4)One approach to analysing some encrypted data where a substitution is suspected is frequency analysis. A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters. In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text.
#Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same.
#Hint: There are many ways to do this. It is obviously a dictionary, but we will want zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so best to ignore that initially, and then check the usual resources for the runes.

def frequency_analysis(message):
    letter_counts = {char: message.lower().count(char) for char in set(message.lower()) if char.isalpha()}
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    print("Six most common letters and their counts:")
    for letter, count in sorted_letters[:6]:
        print(f"{letter}: {count}")

if __name__ == "__main__":
    frequency_analysis(input("Enter a message: "))
