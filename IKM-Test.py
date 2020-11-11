# before = [1,2,3,4,5]
#
# def bar(lst):
#     return lst.append(7)
#
# after = bar(before)
# print(after)

# def sq(x):
#     return x*x
#
# def recursive_map(func, seq):
#     if seq == []:
#         return seq
#     else:
#         return [func(seq[0])]+recursive_map(func,seq[1:])
# print(recursive_map(sq,[1,2,3]))

# x = [1,2,3,4,5]
# print(set(map(lambda num: num*num, x)))

# print([n ** 2 for n in range(10) if n%2])

# print("{0} {1}".format("Welcome and", "Hello World!"))

# class Services:
#     def __init__(self):
#         self.x = 1
#         self.__y = 1
# example = Services

# def foo():
#     raise Exception
# try:
#     foo()
# except BaseException:
#     print(BaseException)


# def f():
#     for i in range(3):
#         yield i
#
# res = list(f())
# print(res)
#
# res2 = []
# g = f()
# while True:
#     try:
#         res2.append(next(g))
#     except StopIteration:
#         break
# print(res2)


# if ((True == False) and (False in (False,))) == False:
#     print("It eval false")
# elif ((True == False) or (False in (False,))) != False:
#     print("it eval true")
# else:
#     print("No eval occur")


# mydict = {1:1,2:2,3:3,4:4,5:5}
# del mydict[5]
# z = {}
# for x in mydict:
#     if x != 5:z[x] = mydict[x]
# mydict = z
# print(z)
# print(mydict)

# req = input("Favorite lang")
# if req == "python":
#     resp = "True"
# else:
#     resp = "False"
# print(resp)

import sys, re
import os
import stat
# f = open("Name.txt", 'r')
# size = f.seek(os.SEEK_SET)
# print(size)
# size = os.stat("Name.txt")[stat.ST_SIZE]
# print(size)


# # pat = re.compile(r"-?[0-9]+")
# # pat = re.compile(r":numer:+")
# # pat = re.compile(r"-*\d*")
# # pat = re.compile(r"[-09]+")
# pat = re.compile(r"-*[-09]+")
# a = pat.fullmatch(str)
# print(a)


# class Ex:
#     n = 2020
#     def foo(self):
#         return "Hello Space"
#
# # Ex.n()
# # print(Ex.foo)
# # Ex.n
# Ex.foo(n)
# # Ex.foo()


# class Foo(object):
#     @classmethod
#     def class_foo(cls):
#         print("Class method for the class: %s" % cls)
# Foo.class_foo()

# class Foo(object):
#     def class_foo(cls):
#         print("Class method for the class: %s" % cls)
#     class_foo = classmethod(class_foo)
# Foo.class_foo()


# import results
# print(results.add(5, 5))

# wordl = ["a","b","c"]
# # wordc = {}
# # for w in wordl:
# #     if w in wordc:
# #         wordc[w]+=1
# #     else:
# #         wordc[w] = 1
# from collections import defaultdict
# wordc = defaultdict(int)
# for w in wordl:
#     wordc[w]+=1
# print(wordc)

# testS = "Yellow Blue Gold Green"
# print(re.search(r'Blue',testS).group(0))
# print(re.search(r'Blue',testS))


# def genadd(x):
#     def addy(y):
#         return x+y
#     return addy
# print(genadd(5))

# add = 0
# def gena(x):
#     global add
#     x = add
#     def addy(y):
#         return add+y
#     return addy
#
# print(gena(5))

# def genadd(x):
#     def add(y,x=x):
#         return x+y
#     return add
#
# print(genadd(6))
#
# def genadd2(x):
#     return lambda x,y:x+y
#
# print(genadd2(6))


# i = 150
# j = 300
# if ((True == False) and (False in (False,))) == True:
#     print(i)
# elif (True == False) in (False,) == False:
#     print(j)
# else:
#     print("No arith")


# def add(o):
#     def inc(nums):
#         numbs = []
#         for n in nums:
#             numbs.append(n+o)
#         return numbs
#     return inc
# var1 = add(5)
# print(var1([23,88]))

# ex = {'OnlineTesting':'Programming', 'ProgrammingLanguages':'Python'}
# print('Services: {OnlineTesting}, {ProgrammingLanguages}'.format(**ex))
#
# tup1 = "Online testing","Programming"
# print(tup1)
#
# x, y = tup1
# print(x)
# print(y)

import Fibon
# def fib(n):
#     v1, v2 = 0, 1
#     while v1 < n:
#         print(v1, end=' ')
#         v1, v2 = v2, v1 + v2
#     print()
#
#
# def bar(n):
#     res = []
#     v1, v2 = 0, 1
#     while v1 < n:
#         res.append(v1)
#         v1, v2 = v2, v1 + v2
#     return res
# print(Fibon.__name__)
# print(Fibon.bar(100))
#
# import random
# string = 'avsdbc'
# n = 3
#
# pw = ''.join(random.sample(string,n))
# print(pw)


# lst = [1,2,3,4,4,5,6,7,7]
# output = []
# for x in lst:
#     if x % 2 == 0:
#         output.append(x)
# print(output)

# class Testing:
#     def __init__(self):
#         self.__score = 95
#
#     def test(self):
#         print("Score: {}".format(self.__score))
#
#     def maxs(self, score):
#         self.__score = score
#         print("Max score is: {}".format(self.__score))
#
# res = Testing()
# res.test()
#
# res.maxs(100)
# res.test()

# n = 12
# names = [[]] * n
#
# emp = "Adam"
# m = 6
# names[m].append(emp)
# print(names)

#
# print("user input")
# line = sys.stdin.readline()

# text = []
# pat = re.compile("[0-9]{5}")
# print(pat.findall(text))

# services = {"Service": "Python Testing", "Version":3,"Results":95}
# print("Service: %s" %services["Service"])
# print("Version: %d" %services["Version"])
# print("Results: %s" %services["Results"])
#
#
# services = {"Service": "Python Testing", "Version":3,"Results":95}
# print("Service: %s" %services{"Service"})


# tot = 0
# for n in range(1,3,2):
#     tot+=n*n
# print(tot)

from string import *
# method = "METHODS"
# def x(methods):
#     method = str.swapcase(methods)
#     print(("%(method)s" % locals()))
# methods = str.swapcase(method[:-1])
# x(methods)


# num = [1,2,3,4]
# res = []
# for x in num:
#     res.append(x**2)
#
# print(res)

# def foo(filename):
#     return filename
# functions["id"]


# class CordsA(object):
#     __slots__ = ["x","y","z"]
#     w=1
#
# class CordsB(CordsA):
#     __slots__ = ["w","z"]
#     pass
# a = CordsA
# b = CordsB
#
# c =b._w=40
# print(c)
# t=a.x=10
# print(t)

# name = 1
# email = 0
# username = 1
# password = 1
# if password == ((name * email) or username):
#     print("User login")
# elif password == ((name * username) and email):
#     print("username re")
# elif password == ((username * email) % name):
#     print("pass req")
# else:
#     print("404")


# class foo(object):
#     def __str__(self):
#         return "testing"
#     def __repr__(self):
#         return "Programming"
#
# print('{0!s} {0!r}'.format(foo()))


# def swap(foo, bar):
#     y = foo;
#     foo = bar;
#     print("Foo inside function : :",foo)
#     print("Bar inside function : ", bar)
#     return (foo,bar)
#
# foo = 5
# bar = 15
# print("foo before sending to function " , foo)
# print("bar before sending to function " , bar)
# x = swap(foo, bar)
# print("foo after sending to function ", x[0])
# print("bar after sending to function ", x[1])
