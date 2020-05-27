#Property use property():we can define property in python
# property :: If we want to access or to initialize the private attribute of class we can use property

class A:
    def __init__(self, name="joshua"):
        self.__name = name

    #Use decorator property
    @property
    def names(self):
        return self.__name

    @names.setter
    def names(self, name):
        self.__name=name

    def setname(self, value):  #Mutator Method
        self.__name = value

    def getname(self):         #Accessor Method
        return self.__name
    #readonly = getname
    #writeonly = setname
    name=property(getname,setname)

# z = A("Zero")
# # print(z.getname())
# print(z.name)
# z.name = "Tony"
# print(z.name)
#
# z.setname("Stark")

#decorator

y = A()
y.name="Yahoo" #set name
print(y.name)