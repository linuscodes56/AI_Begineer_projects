users = [
    {"id": 1, "total": 100, "coupon": "P20" },
    {"id": 2, "total": 150, "coupon": "F10" },
    {"id": 3, "total": 80, "coupon": "P50" },
    {"id": 3, "total": 80, "coupon": "P50" },
    {"id": 3, "total": 80, "coupon": "P00" },
]

discounts = {
    "P20": (0.2, 0),
    "P50": (0, 10), #(percentage on total price, flat discount)
    "F10": (0.5, 0),
    "F00": (0, 0),
}

# task: Calc  money to paid after discounts max

for user in users:
    user_coupon = user["coupon"]
    user_total = user["total"]
    if user_coupon in discounts:
        percentage_discount, flat_discount = discounts[user_coupon]
        discount_1 = 0
        discount_2 = 0
        if percentage_discount != 0:
            discount_1 = user_total * percentage_discount
        if flat_discount != 0:
            discount_2 = flat_discount
        final_discount = max(discount_1, discount_2)
        money_to_paid = user_total - final_discount
        user["final_amount"] = money_to_paid
    else:
        print("User coupon does not exist")

print("Final result ")
print(users)