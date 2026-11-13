import csv
import os

FILENAME = "students.csv"


def initialize_file():
  """Ensures the CSV file exists with proper headers."""
  if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["RollNo", "Name", "Age", "Marks"])


def add_student(roll_no, name, age, marks):
  """Adds a new student record."""
  # Check for duplicate roll number
  if search_student(roll_no, silent=True):
    print(f"Error: Student with Roll No {roll_no} already exists.")
    return

  with open(FILENAME, mode="a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([roll_no, name, age, marks])
  print(f"Student {name} added successfully.")


def view_students():
  """Displays all student records."""
  initialize_file()
  with open(FILENAME, mode="r") as f:
    reader = csv.reader(f)
    data = list(reader)

    if len(data) <= 1:
      print("No student records found.")
      return

    print("\n--- Student Records ---")
    print(f"{'Roll No':<10} | {'Name':<15} | {'Age':<5} | {'Marks':<5}")
    print("-" * 45)
    for row in data[1:]:
      print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<5} | {row[3]:<5}")


def search_student(roll_no, silent=False):
  """Searches for a student by Roll Number."""
  initialize_file()
  with open(FILENAME, mode="r") as f:
    reader = csv.reader(f)
    for row in reader:
      if row and row[0] == str(roll_no):
        if not silent:
          print(
              f"Found: Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Marks:"
              f" {row[3]}"
          )
        return row
  if not silent:
    print(f"Student with Roll No {roll_no} not found.")
  return None


def delete_student(roll_no):
  """Deletes a student record by Roll Number."""
  initialize_file()
  rows = []
  found = False

  with open(FILENAME, mode="r") as f:
    reader = csv.reader(f)
    rows = list(reader)

  new_rows = [rows[0]]  # Keep header
  for row in rows[1:]:
    if row[0] == str(roll_no):
      found = True
    else:
      new_rows.append(row)

  if found:
    with open(FILENAME, mode="w", newline="") as f:
      writer = csv.writer(f)
      writer.writerows(new_rows)
    print(f"Student with Roll No {roll_no} deleted successfully.")
  else:
    print(f"Student with Roll No {roll_no} not found.")


if __name__ == "__main__":
  initialize_file()
  add_student("101", "Alice Smith", 20, 88.5)
  add_student("102", "Bob Jones", 21, 76.0)
  view_students()
  search_student("101")
  delete_student("102")
  view_students()