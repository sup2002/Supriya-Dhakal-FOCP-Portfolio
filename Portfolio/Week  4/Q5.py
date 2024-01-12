#Q)5)Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. 
# Test both functions. (Google will find you the formulae).

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temperature = 25.0
fahrenheit_equivalent = celsius_to_fahrenheit(celsius_temperature)
converted_celsius = fahrenheit_to_celsius(fahrenheit_equivalent)

print(f"{celsius_temperature}°C is equivalent to {fahrenheit_equivalent:.2f}°F")
print(f"{fahrenheit_equivalent:.2f}°F is equivalent to {converted_celsius:.2f}°C")
