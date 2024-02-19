
#_____________________________________________________________________
# Basic OOP

name = "Shane"

# print(type(name))

x = 17

class ThisClass:
    x = 5

# print(ThisClass)

# print(type(ThisClass))
    
# print(x)

# print(ThisClass.x)

#_____________________________________________________________________
#  

class Customer:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    # def __str__(self):
    #     return f"{self.name} is looking for a car and has a budget of {self.budget}."
        
person1 = Customer("Denzel Washington", "40,000")

# print(person1)

#_____________________________________________________________________
# 

class Employee:

    def __init__(self, name, empId, sme): # employee name, employee Id, Subject Matter Expert
            self.name = name
            self.empId = empId
            self.sme = sme

    def __str__(self):
        return f"{self.name} is located in the Diagnosis Dep. He specialises in {self.sme} for Vehicles. If you wish to leave a review, you may reference his Id: {self.empId}."
    
    def available(self):
        return f"{self.name} is available."
    
    def unavailable(self):
        return f"{self.name} is unavailable at this time."
    
emp1 = Employee("Noah Williams", "7652-109-834", "Error Code Analysis")

print(emp1.available())

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

car1 = Car("2007", "BMW", "335i")

car2 = Car("2023", "Chevy", "Corvette")

# print(car1.make)

# print(car2.make)