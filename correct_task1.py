# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_total_and_count(orders):
    total_amount = 0
    valid_orders_count = 0
    for order in orders:
        order["status"] = order["status"].strip().lower()

        if order.get("status") != "canceled":
            total_amount += order.get("amount", 0)
            valid_orders_count += 1
    if (valid_orders_count == 0):
        return 0
    return total_amount/valid_orders_count