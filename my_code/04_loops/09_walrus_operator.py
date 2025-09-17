
# normal code 
value = 13
remainder = value % 5
print(f"Remainder is {remainder}")

# walrus operator
if (remainder2 := value % 5): # evalute expression and assign the value as well 
    print(f"Walrus remainder: {remainder2}")

# if remainder3 = value: # gives SyntaxError
#     print(remainder3)

# use case of walrus operator
# EG 1: Takes input and checks membership in the same line.
# cup_sizes = ["small", "large", "medium"]

# if ((user_cup_choice := input(f"Enter you cup size from: {', '.join(cup_sizes)} \n")) in cup_sizes):
#     print(f" you will get {user_cup_choice} chai")
# else:
#     print(f"{user_cup_choice} cup size does not exist")

# EG2: Keeps asking until user selects a valid flavor.
flavours = ['ginger', 'lemon', 'masala', 'mint']
print(f"Available Flavours: {flavours}")

while ((user_flavour := input(f"Pick flavours from {', '.join(flavours)}: ")) not in flavours):
    print(f"{user_flavour} is not available. Pick again!!!")
else:
    print(f"Flavour available {user_flavour}")