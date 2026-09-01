# Lab Exercise 2: Variables, Operators, and Input/Output
name = input("Enter your name: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Arithmetic operators
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print(f"\nHello, {name}!")
print(f"Addition ({num1} + {num2}) = {addition}")
print(f"Subtraction ({num1} - {num2}) = {subtraction}")
print(f"Multiplication ({num1} * {num2}) = {multiplication}")
print(f"Division ({num1} / {num2}) = {division}")