
def make_chai():
    # return "Here is my masala chai."
    print("Here is my masala chai.") # if fx is not returning value than it will return None implicitly


# print(make_chai())
returned_value = make_chai()
print(returned_value)

# you can return
# 1. one value
# 2. multiple value
# 3. early from a fx

# when returning nothing than implict return of None
def idle_chaiwala():
    pass 

print("idle chaiwala: " ,idle_chaiwala())

# 1. one value returned
def sold_cups():
    return 120

total = sold_cups()
print("total", total)

# 3. early return from fx: once the return is executed, after that remaining fx will not be executed
def chai_status(cup_left):
    if cup_left == 0:
        return "Sorry, No chai cups left"
    return "Here is your chai"
    print("Chai") # this is unreachable code ie short-circuit.

chai_status(0) # 1st return is printed
chai_status(5) # 2nd return is printed 

# 2. return multiple values 
def chai_report():
    return 100, 20 # sold, rem

sold, remaining = chai_report()
print("sold", sold)
print("remaining", remaining)

def chai_report():
    return 100, 20, 1111111 # sold, rem

sold, remaining, _ = chai_report() # _ is used when we dont use the variable value throught out the program, instead use a variable name so that in future it could be used.
print("sold", sold)
print("remaining", remaining)
print("_", _) # mostly never used 
