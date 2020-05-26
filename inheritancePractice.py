class A():
    def __init__(self):
        self.name = 'joshua'
    def view(self):
        print("My name in A is ",self.name)
    def sayHello(self):
        print("Hello there")

class B(A):
    def __init__(self):
        self.name = "JayZ"
        A.__init__(self) #because this is declared after 'joshua' would be used
        self.lastname = "Thao"
    def view(self):
        print(self.name, " ", self.lastname)
    def sayHi(self):
        print("Hi there")

class C(B):
    def function1(self):
        print("Function from C")
    def sayHello(self):
        print("Hello from C class")
        super().sayHello()

o1 = B()
#
o1.view()

o2 = C()
o2.sayHello()