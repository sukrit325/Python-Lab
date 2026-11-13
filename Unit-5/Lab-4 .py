import csv
import matplotlib.pyplot as plt

# Generate sample sales CSV data
sales_data = [
    ["Month", "Sales"],
    ["January", 15000],
    ["February", 18500],
    ["March", 22000],
    ["April", 20000],
    ["May", 25500],
    ["June", 30000],
]

with open("sales.csv", "w", newline="") as file:
  writer = csv.writer(file)
  writer.writerows(sales_data)

# Read CSV and plot dashboard
months = []
sales = []

with open("sales.csv", "r") as file:
  reader = csv.reader(file)
  next(reader)  # Skip header
  for row in reader:
    months.append(row[0])
    sales.append(float(row[1]))

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", color="teal", linestyle="-", linewidth=2)
plt.title("Retail Sales Dashboard")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()