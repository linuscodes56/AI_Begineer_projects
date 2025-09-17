answer = input("Choose snack between cookies, samosa. \n").lower() # normalize the user answer

# if answer in ("cookies", "samosa"):
if answer == "cookies" or answer == "samosa":
    print("Order confirmed")
else:
    print("Order unavailable")