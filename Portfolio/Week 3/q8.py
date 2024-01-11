#Q)8)Modify the "Times Table" again so that the user still enters the number of the table, but if this number is negative the table is printed backwards. So entering "-7" would produce the Seven Times Table starting at "12 times" down to "0 times".

table_number = int(input("Enter the number for the times table (-12 to 12): "))

if -12 <= table_number <= 12:
    step = -1 if table_number < 0 else 1
    for i in range(12 * step, (12 + step * 1), step):
        print(f"{i * step} x {table_number} = {i * table_number}")
else:
    print("Error: Please enter a number between -12 and 12.")
