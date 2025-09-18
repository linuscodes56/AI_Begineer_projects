chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type # access and change the global variable, global keyword can access the global variable, from anywhere in program
        # nonlocal chai_type # will throw error as front_desk() hasa no chai_type variable and nonlocal will only get the just above the scope 
        chai_type = "Irani"
        print(chai_type)
    kitchen()

front_desk()
print(chai_type)