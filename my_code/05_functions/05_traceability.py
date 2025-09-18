def add_vat(price, vat_rate):
    return price + price * vat_rate/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original value: {price}, final with VAT: {final_amount}")

