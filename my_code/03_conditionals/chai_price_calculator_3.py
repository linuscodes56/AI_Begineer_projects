order_size = input("Tea: small, medium, large? \n").lower()

if order_size == "small":
    print(f"{order_size} Tea is Rs 10")
elif order_size == "medium":
    print(f"{order_size} Tea is Rs 15")
elif order_size == "large":
    print(f"{order_size} Tea is Rs 20")
else:
    print("Unknown Cup size")