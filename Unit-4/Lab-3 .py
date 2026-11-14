import csv
import os

filename = "payroll.csv"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    deduction = float(input("Enter Deduction: "))

    net = basic + allowance - deduction

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, basic, allowance, deduction, net])

    print("Employee added successfully.")
    print("Net Salary:", net)

def view_payroll():
    if not os.path.exists(filename):
        print("No payroll records found.")
        return

    total = 0

    with open(filename, "r") as f:
        reader = csv.reader(f)

        print("\n--- PAYROLL REPORT ---")

        for row in reader:
            print(row)
            if row[0] != "EmpID":
                total += float(row[5])

    print("Total Monthly Payout: ₹", total)

while True:
    print("\n1. Add Employee")
    print("2. View Payroll")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_payroll()
    elif choice == "3":
        print("Exiting Payroll System...")
        break
    else:
        print("Invalid choice.")
