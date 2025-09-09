
# class 
class Chai:

    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness # attributes
        self.milk_level = milk_level

    # methods
    def sip(self):
        print("sipping chai")

    def add_sugar(self, amount):
        print("added the sugar")

# object
my_chai = Chai(sweetness=3, milk_level=2)
my_chai.sip()
my_chai.add_sugar(3)
