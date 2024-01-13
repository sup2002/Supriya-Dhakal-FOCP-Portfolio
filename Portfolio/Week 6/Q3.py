#Q)3)Write and test a function that determines if a given integer is a prime number.
# A prime number is an integer greater than 1 that cannot be produced by multiplying two other integers.

def is_prime_from_user():
    try:
        number = int(input("Enter an integer: "))
        return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Example usage:
result = is_prime_from_user()
if result is not None:
    print(f"The entered number is {'prime' if result else 'not prime'}.")
