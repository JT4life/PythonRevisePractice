
#Not finish
# email = input("Enter your email address")
# b = email.isalpha()
# if "@" in email:
#     a = email.index("@")
#     print(a)
#     print(b)
#     name = []
#     for i in range(0,a):
#         print(name.append(i))

#2 done
# def square():
# #     for i in range(1,21):
# #         while i > 5:
# #             i *= i
# #             print(i)
# #             break
# # square()

#3 done
# def readWords():
#     enter = input("Write some words")
#     count = dict()
#     split = enter.split()
#
#     for word in split:
#         if word in count:
#             count[word] +=1
#         else:
#             count[word] = 1
#     return count
#
# print(readWords())


#4

#5 not done
# def tup():
#     listNames = []
#     listAge = []
#     listScore = []
#     inp = False
#     while inp == False:
#         inp = input("Enter your name, age, and score separated by spaces, enter blank line to exit")
#
# tup()

#6 partial finish
# def account():
#     total = 0.0
#     dep = float(input("How much money to deposit? Or 0 to cancel"))
#     while dep:
#         total += dep
#         break
#     w = float(input("How much money to withdraw? Or c to cancel"))
#     while w:
#         total -= w
#         break
#     print("total remaining is ", total)
#
# account()

#7 done
# def cases():
#     lower = 0
#     upper = 0
#     userEnter = input("Enter a sentence with upper and lower case letters")
#     for i in userEnter:
#         if i.isupper():
#             upper += 1
#         if i.islower():
#             lower += 1
#     print("Lower case", lower, "Upper case", upper)
#
# cases()

#8
# def find():
#     for i in range(1000, 3001, 2):
#         print(i, end=",")
# find()

#9

#10
def xy(x, y):
    arr = []
    add = []
    for i in range(x):
        arr.insert(0, i)
        for j in range(y):
            add.append(j)
    print(arr,add)

xy(3,5)