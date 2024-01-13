#Q)2)Write and test a function that takes an integer as its parameter and returns the factors of that integer. 
# (A factor is an integer which can be multiplied by another to yield the original).

def find_factors_from_user():
    try:
        n = int(input("Enter an integer: "))
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    except ValueError:
        print("Invalid input. Please enter an integer.")

factors_of_user_input = find_factors_from_user()
if factors_of_user_input:
    print(f"The factors are: {factors_of_user_input}")

