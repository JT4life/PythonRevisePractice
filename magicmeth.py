class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):  #if . included return float
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other): #reflect magic method
        return self + other

    def __iadd__(self, other): #in place magic method
        self.value = self+other
        return self.value


a = NumString(5)
print(a + 5)
b = NumString(2.2)
print(b + 3)

#magic method test
# >>> from magicmeth import NumString
# >>> age = NumString(5)
# >>> age+5
# 10
# >>> 5+age
# 10
# >>> age +=1
# >>> age
# 6
# >>>

