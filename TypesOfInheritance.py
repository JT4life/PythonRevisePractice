# class Parent:
#     def func1(self):
#         print('this is parent function')
#
# class Child(Parent):
#     def func2(self):
#         print('this is child function')
#
# ob = Child()
#
# ob.func1()
# ob.func2()

#with __init__ functions
# class Parent:
#     def __init__(self,fname, fage):
#         self.name = fname
#         self.age = fage
#
#     def view(self):
#         print(self.name, self.age)
#
#
# class Child(Parent):
#     def __init__(self, fname, fage):
#         Parent.__init__(self, fname, fage)
#         self.lastname = "Thao"
#
#
#     def view(self):
#         print(self.age, self.lastname, self.name)
#
# ob1 = Child(23,'joe')
# ob1.view()

class Parent:
    def f1(self):
        print("This is function 1")

class Parent2(Parent):
    def f3(self):
        print("This is function 3 from Parent2")

# class Child(Parent, Parent2): #example of multiple inheritance
#     def f2(self):
#         print("This is function 2")

# class Child(Parent2): #multi level inheritance example
#     def f2(self):
#         print("This is function 1")

# class Child(Parent): #hierachel inheritance
#     def f2(self):
#         print("This is function 1")
class Parent3:
    def f4(self):
        print("This is function 4 from Parent3")

class Child(Parent, Parent3): #hybrid inheritance
    def f2(self):
        # super().f1() #calls directly from Parent
        print("This is function 2")

    def f1(self):
        print("Override parent function 1")
obj = Child()

obj.f1()
