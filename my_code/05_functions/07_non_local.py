
# nonlocal keyword usage 

chai_type = 'global'

def update_order():
    chai_type = "Elachi"
    print(f"Before kitchen() update: {chai_type}")

    def kitchen():
        nonlocal chai_type # it will change the variable just ouside of the scope.
        # global chai_type # will change the global variable and not the next outside fx's variable
        chai_type = "Kesar" # if nonlocal keyword is not used than outer scoped variable value will not be changed
    
    kitchen()
    print(f"After kitchen() update: {chai_type}")

update_order()
# print(f"Global: {chai_type}")