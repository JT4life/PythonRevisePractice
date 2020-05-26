def swapit(x, y):
    return y,x

swap = (lambda x,y : swapit(x,y))

print(swap(4,7))

swap1=lambda no1,no2: (no2,no1)
print(swap1(2,4))