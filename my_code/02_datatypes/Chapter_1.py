# immutable examples 

sugar_amount = 2
print(f"Inital sugar: {sugar_amount}")
print(f"identity 1: {id(sugar_amount)}")

sugar_amount = 12
print(f"Second Inital sugar: {sugar_amount}")
print(f"identity 2: {id(sugar_amount)}") # never check if variable is mutable or not with value, check with id. 

# tuple eg
tup = tuple(())
print(f"Initial ID: {id(tup)}")

tup = tuple((1,2))
print(f"Second ID: {id(tup)}") # id changed
