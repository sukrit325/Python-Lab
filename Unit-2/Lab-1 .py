import random

print("--- Number Guessing Game ---")
target_number = random.randint(1, 50)
attempts = 0

while True:
  guess = int(input("Guess a number between 1 and 50: "))
  attempts += 1

  if guess < target_number:
    print("Too low! Try again.")
  elif guess > target_number:
    print("Too high! Try again.")
  else:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    break