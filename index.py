orders = [180, 220, 150, 300, 180, 250, 200]

revenue = 0
orders_count = 0

for order in orders:
    revenue += order
    orders_count += 1

print(revenue)
print(orders_count)
