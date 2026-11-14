import csv
import os

filename = "students.csv"
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, age, marks])

    print("Student added successfully.")

def view_students():
    if not os.path.exists(filename):
        print("No records found.")
        return

    with open(filename, "r") as f:
        reader = csv.reader(f)
        print("\n--- STUDENT RECORDS ---")
        for row in reader:
            print(row)

def search_student():
    roll = input("Enter Roll Number to search: ")

    if os.path.exists(filename):
        with open(filename, "r") as f:
            for row in csv.reader(f):
                if row[0] == roll:
                    print("Student Found:", row)
                    return

    print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if not os.path.exists(filename):
        print("No records found.")
        return

    with open(filename, "r") as f:
        rows = list(csv.reader(f))

    new_rows = [row for row in rows if row[0] != roll]

    if len(rows) == len(new_rows):
        print("Student not found.")
    else:
        with open(filename, "w", newline="") as f:
            csv.writer(f).writerows(new_rows)
        print("Student deleted successfully.")

while True:
    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
