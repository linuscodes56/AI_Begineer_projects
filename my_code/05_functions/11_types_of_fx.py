# pure fxs
def pure_chai(cups):
    return cups * 10

#impure fx
total_chai = 0

#  not recommended: as we are chainging the global variable
def impure_chai(cups):
    global total_chai
    total_chai += cups # chainging the global variable

# recursive fxs
def pour_chai(n):
    if n == 0:
        return
    
    print(f"Pouring cup number: {n}")
    pour_chai(n-1)

pour_chai(4)

# lambdas/anonamous fx
chai_type = ["light", "kadak", "ginger", "kadak"]


# filter() applies the lambda to each element, keeping only those where the condition is true.
strong_chai = list(filter(lambda chai: chai != "kadak" , chai_type))
print(strong_chai)

# Using Lambda for Filtering
# Lambda takes a single argument—each element being iterated (called chai here).
# Returns True if element matches condition (chai == 'karak chai'), else False.
# Filtered results stored as a list.
