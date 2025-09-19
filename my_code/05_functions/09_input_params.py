# passing immutable datatype
chai = "Ginger Chai"

def prepare_chai(order):
    print(f"Preparing: ", order)
    # order[1] = 'd' # can't change

prepare_chai(chai)
print(chai)

# if passed mutables datatypes than inner values could be changed
chai_cups = [1, 2, 3]

def edit_chai(cups):
    cups[1] = 42


print(chai_cups)
edit_chai(chai_cups)
print(chai_cups)

## args and *kwargs

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# two ways of passing arguments
make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Medium", milk="No") # keyword

# prod method
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients) # tuples
    print("Extras", extras) # dict

special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="No")


# gotchas in python while having default params

def chai_order(order="Hitesh"): #immutable args are ok when passing
    pass

def chai_order2(order=[]):
    order.append(1)
    print(order)
    
# when calling this 2 times than see the list values, mutables list will be updated
chai_order2()
chai_order2()

# sol
def chai_order_sol(order=None):
    if order is None:
        order = []
    order.append(1)
    print(order)
    
# when calling this 2 times than see the list values, mutables list will be updated
chai_order_sol()
chai_order_sol()


