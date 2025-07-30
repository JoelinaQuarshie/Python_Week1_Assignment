# Welcome to the calculator module!

# Step 1: Enter the first number
first_number = float(input("Enter the first number: "))

# Step 2: Enter the second number
second_number = float(input("Enter the second number: "))

# Step 3: Choose the operation
operation = input("Choose an operation (+, -, *, /): ")

# Step 4: Perform the calculation

# Addition
if operation == '+':
    result = first_number + second_number 

# Subtraction
elif operation == '-':
    result = first_number - second_number

# Multiplication
elif operation == '*':
    result = first_number * second_number

# Division
elif operation == '/':
    if second_number == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = first_number / second_number

print(f"The result of {first_number} {operation} {second_number} is: {result}")
