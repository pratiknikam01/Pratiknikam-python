import math

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b

# Function for square
def square(a):
    return a ** 2

# Function for square root
def square_root(a):
    return math.sqrt(a)

# Display menu
print("----- SCIENTIFIC CALCULATOR -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Square Root")

choice = int(input("Enter your choice: "))

# Perform operation
if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", add(a, b))

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", subtract(a, b))

elif choice == 3:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", multiply(a, b))

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b != 0:
        print("Result =", divide(a, b))
    else:
        print("Cannot divide by zero")

elif choice == 5:
    a = float(input("Enter a number: "))
    print("Square =", square(a))

elif choice == 6:
    a = float(input("Enter a number: "))

    if a >= 0:
        print("Square Root =", square_root(a))
    else:
        print("Square root is not possible")

else:
    print("Invalid choice")