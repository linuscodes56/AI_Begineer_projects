
# returning value from fx
def calc_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calc_bill(3, 15)
print(my_bill)
print(f"Bill for table 2: {calc_bill(2, 50)}")

