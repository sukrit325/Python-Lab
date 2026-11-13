import random


def roll_dice(num_dice=1):
  return [random.randint(1, 6) for _ in range(num_dice)]


def simulate_rolls(num_rolls, num_dice=1):
  results = {i: 0 for i in range(num_dice, num_dice * 6 + 1)}
  for _ in range(num_rolls):
    total = sum(roll_dice(num_dice))
    results[total] += 1
  return results