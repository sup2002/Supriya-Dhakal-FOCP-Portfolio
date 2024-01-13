#Q)1)Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).
#Hint: This is in many ways a trick question. Think!

def int_to_binary_from_user():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            raise ValueError("Input must be a positive integer.")
        elif n == 0:
            return "0b0"
        else:
            return bin(n)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

binary_representation = int_to_binary_from_user()
if binary_representation:
    print(f"The binary representation is: {binary_representation}")

