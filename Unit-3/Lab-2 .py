def calculate_grade(score):
  """Determines letter grade based on score."""
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"


def process_student_grades(student_records):
  """Processes scores and prints a formatted grading report."""
  print("\n--- Student Grading Report ---")
  print(f"{'Name':<15} | {'Scores':<20} | {'Average':<8} | {'Grade':<6}")
  print("-" * 60)

  for name, scores in student_records.items():
    avg = sum(scores) / len(scores) if scores else 0
    grade = calculate_grade(avg)
    scores_str = ", ".join(map(str, scores))
    print(f"{name:<15} | {scores_str:<20} | {avg:<8.2f} | {grade:<6}")


if __name__ == "__main__":
  students = {
      "Alice": [85, 90, 88],
      "Bob": [72, 65, 70],
      "Charlie": [95, 92, 98],
      "Diana": [55, 60, 58],
  }
  process_student_grades(students)