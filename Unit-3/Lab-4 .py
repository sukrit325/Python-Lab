def analyze_sales_data(sales_records):
  """Analyzes sales transactions and prints a performance summary."""
  total_revenue = 0
  item_sales = {}
  daily_revenue = {}

  for record in sales_records:
    date = record["date"]
    item = record["item"]
    quantity = record["quantity"]
    price = record["price"]

    revenue = quantity * price
    total_revenue += revenue

    # Item aggregation
    if item in item_sales:
      item_sales[item]["quantity"] += quantity
      item_sales[item]["revenue"] += revenue
    else:
      item_sales[item] = {"quantity": quantity, "revenue": revenue}

    # Daily aggregation
    daily_revenue[date] = daily_revenue.get(date, 0) + revenue

  best_item_qty = max(item_sales.items(), key=lambda x: x[1]["quantity"])
  best_item_rev = max(item_sales.items(), key=lambda x: x[1]["revenue"])

  print("\n--- Sales Data Analysis Report ---")
  print(f"Total Company Revenue: ${total_revenue:.2f}")
  print(
      f"Best Selling Item (by Qty): {best_item_qty[0]}"
      f" ({best_item_qty[1]['quantity']} units)"
  )
  print(
      f"Top Revenue Item: {best_item_rev[0]} (${best_item_rev[1]['revenue']:.2f})"
  )

  print("\nDaily Breakdown:")
  for date, rev in sorted(daily_revenue.items()):
    print(f"  {date}: ${rev:.2f}")


if __name__ == "__main__":
  transactions = [
      {"date": "2026-06-01", "item": "Laptop", "quantity": 2, "price": 1200.00},
      {"date": "2026-06-01", "item": "Mouse", "quantity": 10, "price": 25.50},
      {"date": "2026-06-02", "item": "Keyboard", "quantity": 5, "price": 45.00},
      {"date": "2026-06-02", "item": "Laptop", "quantity": 1, "price": 1200.00},
      {"date": "2026-06-03", "item": "Monitor", "quantity": 3, "price": 300.00},
      {"date": "2026-06-03", "item": "Mouse", "quantity": 4, "price": 25.50},
  ]
  analyze_sales_data(transactions)