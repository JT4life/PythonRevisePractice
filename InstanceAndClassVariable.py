#Types of variables in a class
#1. Instance variable : Belongs to instance     2. Class variable aka Static variable : Belongs to class

class A:
    #class variable
    address = "USA"

    def __init__(self):
        self.name = "Peter" #instance variables
        self.number = 6519995888

obj = A()
obj1 = A()

print(obj.name, " ", obj.number)
print(obj1.name, " ", obj1.number)
obj.name = "Adam"
obj.number = 9998885555
obj1.name = "Link"
obj1.number = 1119998888
# A.address = "India"

obj1.address = "Mexico"
print(obj.name, " ", obj.number, " ", obj.address)
print(obj1.name, " ", obj1.number, " ", obj1.address)

print(A.address)