import csv
import matplotlib.pyplot as plt

months = []
sales = []

n = int(input("Enter number of months: "))

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Sales"])

    for i in range(n):
        month = input("Enter month: ")
        amount = float(input("Enter sales: "))
        writer.writerow([month, amount])

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        months.append(row[0])
        sales.append(float(row[1]))

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", color="teal",
         linestyle="-", linewidth=2)

plt.title("Retail Sales Dashboard")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()