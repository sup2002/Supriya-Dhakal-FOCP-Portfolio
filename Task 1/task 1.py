def get_order_details():
    while True:
        try:
            # Get the number of pizzas ordered
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas < 0:
                raise ValueError("Please enter a positive integer!")

            # Check if delivery is required
            delivery_required = input("Is delivery required? (Y/N) ").upper()
            if delivery_required not in ["Y", "N"]:
                raise ValueError("Please answer 'Y' or 'N'.")

            # Check if it is Tuesday
            is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
            if is_tuesday not in ["Y", "N"]:
                raise ValueError("Please answer 'Y' or 'N'.")

            # Check if the app was used
            used_app = input("Did the customer use the app? (Y/N) ").upper()
            if used_app not in ["Y", "N"]:
                raise ValueError("Please answer 'Y' or 'N'.")

            return num_pizzas, delivery_required, is_tuesday, used_app

        except ValueError as error:
            print(error)

def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    # Initial pizza price without any discounts
    pizza_price = 12
    # Initial delivery cost
    delivery_cost = 2.5

    # Apply Tuesday discount
    if is_tuesday == "Y":
        pizza_price /= 2

    # Calculate total pizza price without delivery cost
    total_pizza_price = num_pizzas * pizza_price

    # Apply delivery cost if required
    if delivery_required == "Y":
        # If there are five or more pizzas, delivery is free
        if num_pizzas >= 5:
            delivery_cost = 0
        total_pizza_price += delivery_cost

    # Apply app discount
    if used_app == "Y":
        # 25% discount after Tuesday discount
        total_pizza_price *= 0.75

    # Round total price to two decimal places
    return round(total_pizza_price, 2)

def main():
    print("BPP Pizza Price Calculator")
    print("==========================\n")

    # Get order details from the user
    num_pizzas, delivery_required, is_tuesday, used_app = get_order_details()

    # Calculate and display the total price
    total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)
    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
