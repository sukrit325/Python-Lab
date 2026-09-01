# Lab Exercise 3 Part A: Simple Calculator
print("--- Simple Calculator ---")
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
  print(f"Result: {a + b}")
elif op == "-":
  print(f"Result: {a - b}")
elif op == "*":
  print(f"Result: {a * b}")
elif op == "/":
  if b != 0:
    print(f"Result: {a / b}")
  else:
    print("Error: Division by zero is not allowed.")
else:
  print("Invalid operator entered.")

# Lab Exercise 3 Part B: Area Calculation
print("\n--- Area Calculator ---")
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
print(f"Area of Rectangle: {length * width}")

radius = float(input("Enter radius of the circle: "))
area_circle = 3.14159 * (radius**2)
print(f"Area of Circle: {area_circle:.2f}")