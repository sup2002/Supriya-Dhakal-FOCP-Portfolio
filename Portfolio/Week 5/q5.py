#Q)5)Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed the maximum, minimum, and mean. 
# Create a version of that program that takes the values from the command-line instead. 
# Be sure to handle the case where no arguments are provided!

import sys

temperatures = sys.argv[1:]
if not temperatures:
    print("No temperatures provided.")
else:
    try:
        temperatures = list(map(float, temperatures))
        print(f"Max: {max(temperatures):.2f}C, Min: {min(temperatures):.2f}C, Mean: {sum(temperatures) / len(temperatures):.2f}C")
    except ValueError:
        print("Invalid temperature values. Please provide numerical values.")
