#Q)8)Modify the previous program so that it can process any number of values. The input terminates when the user just pressed "Enter" at the prompt rather than entering a value.

temperatures = []

while (input_str := input("Enter temperature in centigrade (press Enter to finish): ").strip()):
    if input_str[:-1].isdigit() and input_str.endswith('C'):
        temperatures.append(float(input_str[:-1]))
    else:
        print(f"Ignored invalid input: {input_str}. Please use the format 'numberC'.")

if temperatures:
    print(f"Maximum temperature: {max(temperatures):.2f}C")
    print(f"Minimum temperature: {min(temperatures):.2f}C")
    print(f"Mean temperature: {sum(temperatures) / len(temperatures):.2f}C")
else:
    print("No valid temperatures entered.")
