# flavours = ["ginger", "turmeric" "Out of stock", "Lemon" , "Discontinued", "Tulsi"] # if i missed the comma then i have undefiend behaviour of string while printing 
flavours = ["ginger", "turmeric", "Out of stock", "Lemon" , "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    elif flavour == "Discontinued":
        break
    print(f"tea flavour: {flavour}")


# Chapter 8: for else
# for else
staff = [("Amit", 16), ("Zara", 17), ("Raj", 63)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff") # else will execute when for loop is fully completed and no break statement was executed 
