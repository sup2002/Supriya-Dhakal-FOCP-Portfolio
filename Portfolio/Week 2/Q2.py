#Q)2)Write a program that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit, like so:
#Enter a temperature in Celsius: 32.5
#32.5C is equivalent to 90.5F.

celsius_temperature = float(input("Enter a temperature in Celsius: "))

# Converting Celsius to Fahrenheit

fahrenheit_temperature = (9/5) * celsius_temperature + 32

print(f"{celsius_temperature}°C is equivalent to {fahrenheit_temperature:.1f}°F.")