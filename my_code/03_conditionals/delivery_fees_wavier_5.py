order_amount = int(input("Order amount? "))

print(f"Delivery is {'free' if order_amount > 300 else '30 Rs'}")