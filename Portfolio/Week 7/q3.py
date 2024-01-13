#Q)3)Write a program that manages a list of countries and their capital cities. It should prompt the user to enter the name of a country.
# If the program already "knows" the name of the capital city, it should display it.
# Otherwise it should ask the user to enter it. This should carry on until the user terminates the program (how this happens is up to you).
#Note: A good solution to this task will be able to cope with the country being entered variously as, 
# for example, "Wales", "wales", "WALES" and so on

def main():
    country_capital_dict = {}

    while True:
        country = input("Enter a country (or 'exit' to end): ").strip().lower()

        if country == 'exit':
            break

        capital = country_capital_dict.get(country, input(f"Enter the capital of {country.capitalize()}: ").strip())
        print(f"The capital of {country.capitalize()} is {capital}.")

if __name__ == "__main__":
    main()
