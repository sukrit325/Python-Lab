import csv
import os

PAYROLL_FILE = "payroll.csv"


def initialize_payroll():
  """Initializes the payroll CSV file if it doesn't exist."""
  if not os.path.exists(PAYROLL_FILE):
    with open(PAYROLL_FILE, mode="w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(
          ["EmpID", "Name", "BasicSalary", "Allowances", "Deductions", "NetSalary"]
      )


def add_employee(emp_id, name, basic, allowances, deductions):
  """Calculates net salary and records the employee data."""
  net_salary = float(basic) + float(allowances) - float(deductions)
  with open(PAYROLL_FILE, mode="a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([emp_id, name, basic, allowances, deductions, net_salary])
  print(f"Payroll record added for {name}. Net Salary: {net_salary}")


def generate_payroll_report():
  """Generates and prints a complete payroll report."""
  initialize_payroll()
  print("\n--- Company Payroll Report ---")
  print(
      f"{'ID':<6} | {'Name':<15} | {'Basic':<10} | {'Allow':<8} |"
      f" {'Deduct':<8} | {'Net Salary':<10}"
  )
  print("-" * 65)

  total_payout = 0.0
  with open(PAYROLL_FILE, mode="r") as f:
    reader = csv.reader(f)
    data = list(reader)
    if len(data) <= 1:
      print("No records available.")
      return

    for row in data[1:]:
      print(
          f"{row[0]:<6} | {row[1]:<15} | {row[2]:<10} | {row[3]:<8} |"
          f" {row[4]:<8} | {row[5]:<10}"
      )
      total_payout += float(row[5])

  print("-" * 65)
  print(f"Total Monthly Payout: {total_payout:.2f}")


if __name__ == "__main__":
  initialize_payroll()
  # Clear existing dummy records for test run clarity if needed
  with open(PAYROLL_FILE, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(
        ["EmpID", "Name", "BasicSalary", "Allowances", "Deductions", "NetSalary"]
    )

  add_employee("E001", "Alice Vance", 50000, 12000, 5000)
  add_employee("E002", "David Miller", 65000, 15000, 7000)
  add_employee("E003", "Emma Watson", 45000, 10000, 4000)
  generate_payroll_report()