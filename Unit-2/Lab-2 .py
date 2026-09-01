# Part A: Prime Number Check
print("--- Prime Number Checker ---")
num = int(input("Enter an integer to check for prime: "))
is_prime = True

if num <= 1:
  is_prime = False
else:
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      is_prime = False
      break

if is_prime:
  print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")

# Part B: Factorial Calculation
print("\n--- Factorial Calculator ---")
fact_num = int(input("Enter a non-negative integer for factorial: "))
factorial = 1

if fact_num < 0:
  print("Factorial is not defined for negative numbers.")
else:
  for i in range(1, fact_num + 1):
    factorial *= i
  print(f"The factorial of {fact_num} is {factorial}.")