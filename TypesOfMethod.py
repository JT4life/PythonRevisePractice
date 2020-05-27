#Types of method
#1. instance method 2. class method 3. static method

class A: #instance method
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sums(self):
        print(self.m1+self.m2)

# z = A(22,33)
# z.sums()

class B: #class method
    country = "USA"

    @classmethod
    def cinfo(cls):
        print(cls.country)

obj = B()
obj.cinfo()