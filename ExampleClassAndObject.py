# 4. WRITE THE EXAMPLE CLASS AND OBJECT
# #             ---CONSTR | METHOD OVERLODING
# #             ---INHERITENCE | METHOD OVERRDIING

class Monkey:
    def __init__(self, age):
        self.color = "brown"
        self.age = age

    def printInfo(self):
        print(self.color,self.age)

    def sayHi(self, greeting=None): #Method overloading
        if greeting is not None:
            print("Hi hi hi" + greeting)
        else:
            print("Hello only")

class babyMonkey(Monkey):
    def __init__(self): #override
        self.age = 1
        self.color = "light brown"

class borrowMonkey(Monkey):
    def __init__(self):
        Monkey.__init__(self,age=3) #change age borrow brown color from Parent

big = Monkey(25)
big.printInfo()
big.sayHi()
big.sayHi("Helllooo")

b = babyMonkey()
b.printInfo()

borrow = borrowMonkey()
borrow.printInfo()