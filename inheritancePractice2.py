class Person:
    def __init__(self):
        self.name = "Parent"

    def names(self):
        print("Names from Person")

class Theif:
    def __init__(self):
        self.name = "Theif"

    def names(self):
        print("Names from Theif")

class Both(Person, Theif):
    def __init__(self):
        self.name = "Both"
        super().__init__()

o = Both()
print(o.name)

o.names()