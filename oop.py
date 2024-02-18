
#_____________________________________________________________________
# Basic OOP

name = "Shane"

# print(type(name))


class ThisClass:
    x = 5

# print(ThisClass)

# print(type(ThisClass))

# print(ThisClass.x)

#_____________________________________________________________________
#  

class Grocery:

    def __init__(self, category, quantity):
        self.category = category
        self.quantity = quantity






#_____________________________________________________________________
# 





#_____________________________________________________________________
# 





#_____________________________________________________________________
# Example
class Car:

    def __init__(self, year, make, model):
        
        self.year = year
        self.make = make
        self.model = model
        
    def __str__(self):
        return f"{self.model}({self.year})" 
    
    def drive(self):
        print("The"+ self.model +"is currently driving.")

    def slow(self):
        print("The"+ self.model +"is slowing down.")

