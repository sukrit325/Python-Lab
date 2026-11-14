import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]


def simulate_rolls(num_rolls, num_dice):
    results = {}

    for i in range(num_rolls):
        total = sum(roll_dice(num_dice))
        results[total] = results.get(total, 0) + 1

    print("\n--- DICE ROLL RESULTS ---")
    for number, count in sorted(results.items()):
        print(f"{number}: {count} times")


num_dice = int(input("Enter number of dice: "))
num_rolls = int(input("Enter number of rolls: "))

simulate_rolls(num_rolls, num_dice)