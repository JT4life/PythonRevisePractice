# def display(): #without params
#     number1=int(input("Enter a number"))
#     number2=int(input("Enter a number"))
#     sum = number1+number2
#     print(sum)
#
# display()

# def display2(number1, number2): #with params
#     sum = number1+number2
#     print(sum)
#
# display2(5,6)

# def display3(number1, number2): #return
#     sum = number1+number2
#     return sum
#
# p = display3(5,6)
# print(p)

#Default value params
# def display3(n1=0,m1=200):
#     sum = n1+m1
#     print("sum of ", n1, " and ", m1, " is ", sum)
# 
# display3()
# display3(11)
# display3(20,m1=30)

# def display4(*args): # Arbitary argument, any number of params you can pass
#     sum = 0
#     for i in args:
#         sum = sum+i
#     print(sum)
#
# display4(10,15,25,25)

# def display5(**kwargs): # any number of key value arguments
#     for k,v in kwargs.items():
#         print(k, v)
#
# display5(name="Joshua",city="St Paul", address="123")

def isNumPrime(): #Prime number
    num = int(input("Enter a number"))
    for i in range(2,num):
        if(num % i) == 0:
            print("number is composite", num)
            break
    else:
        print("number is prime", num)
isNumPrime()

def OddEven(list): #Check list for odd and even numbers
    odd = []
    even = []

    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("odds in list ", odd)
    print('evens in list ', even)

list = [22,14,13,1,5]
OddEven(list)