tea_menu = ["Ginger Tea", "Elachi Tea", "Biscuit", "Cookies"]

for i,item in enumerate(tea_menu, start=1): # tuple is returned (i, item), so unpacking happens on the fly
    print(f"{i}. {item}")