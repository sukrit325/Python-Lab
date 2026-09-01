# Mini Project: Bill Generator
print("--- Store Bill Generator ---")
items = []
grand_total = 0

n = int(input("Enter the number of distinct items purchased: "))
for i in range(n):
  print(f"\nItem {i+1}:")
  item_name = input("  Enter item name: ")
  item_price = float(input("  Enter price per unit: "))
  item_qty = int(input("  Enter quantity: "))

  total_cost = item_price * item_qty
  items.append({"name": item_name, "price": item_price, "qty": item_qty, "total": total_cost})
  grand_total += total_cost

print("\n" + "=" * 40)
print(f"{'INVOICE':^40}")
print("=" * 40)
print(f"{'Item':<15} {'Price':<10} {'Qty':<5} {'Total':<10}")
print("-" * 40)

for item in items:
  print(f"{item['name']:<15} {item['price']:<10.2f} {item['qty']:<5} {item['total']:<10.2f}")

print("-" * 40)
print(f"{'Grand Total:':<30} {grand_total:.2f}")
print("=" * 40)
print("Thank you for your purchase!")