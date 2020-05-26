#number of n digits which are equal to sum of nth power of digits
#E.G 22 so 2^2 = 4 2^2 =4, 4+4=8 8 does not equal 22 thus not armstrong

userEnter = input("Enter digits separated by commas to check if armstrong number") #123
def arm(userEnter):
    split = userEnter.split(',')
    print(split)
    size = len(split)
    print(size)
    newList = []
    toString = ""

    for i in split:
        powered = int(i)**size
        newList.append(powered)
        print(newList)
    totalSum = sum(newList)
    print(totalSum)
    for i in split:
        toString+=i
    if totalSum == int(toString):
        print(totalSum, " Armstrong number = ", toString)
    else:
        print(totalSum, " Not Armstrong number ", toString)
arm(userEnter)

