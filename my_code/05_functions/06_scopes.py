def serve_chai():
    chai_type = "Masala" # local scope: declared inside of fx
    print(f"Inside fx: {chai_type}")

chai_type = "Lemon" #global scope
serve_chai()
print(f"Outside fx: {chai_type}")

def chai_counter():
    chai_order = "mint" #Enclosing scope: scope of outer fx

    def print_order():
        chai_order = "Ginger" # scope of inner nested fx
        print("Inner nested fx call:", chai_order)
    print_order() # declaring a fx from within a fx and calling it inside a fx

    print("Outer nested fx call: ", chai_order)


chai_order = "Tulsi" #Global scope
chai_counter()
print(f"Global scope: {chai_order}")