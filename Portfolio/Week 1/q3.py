#Q)3)Over the summer, temperatures in Yorkshire reached 38.4C.
# Write a program that converts this value in Celsius to the equivalent temperature in Fahrenheit, and then displays both.

# Updated variable names
original_temperature_celsius = 38.4

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius_temp):
    return (9/5) * celsius_temp + 32

# Calculate Fahrenheit temperature
converted_temperature_fahrenheit = convert_to_fahrenheit(original_temperature_celsius)

# Displaying both temperatures with updated strings
print(f"Original Temperature in Celsius: {original_temperature_celsius}°C")
print(f"Converted Temperature in Fahrenheit: {converted_temperature_fahrenheit}°F")
