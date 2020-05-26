# Enter a number , check number is Armstrong Number or not
# Given a number x, determine whether the given number is Armstrong number or not.
# A positive integer of n digits is called an Armstrong number of order n
# (order is number of digits) if.
#
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
#
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# def amrstrong(a,b,c):
#     a1 = a ** 3
#     b1 = b ** 3
#     c1 = c ** 3
#     print(a1,b1,c1)
#     total = str(a1+b1+c1)
#     print(total)
#     print(a,b,c)
#     try:
#         for i in total:
#             if i == a
#
#             print("Armstrong")
#         else:
#             print("Not Armstrong")
#     except:
#         print("error occurred")
# # amrstrong(1,2,0)
# amrstrong(1,5,3)

# Q-2
# Print all Prime numbers from particular range
# Given two positive integer start and end.

# def prime(start, end):
#     if start >= 2 and (end >= 2 and end != start):
#         for number in range(start, end):
#             for devisers in range(2, number):
#                 if number % devisers == 0:
#                     print(number, 'is Not a prime number.')
#                     break
#             else:
#                 print(number, 'is a prime number.')
# prime(2,8)

# Q-3
# Write Program for n-th Fibonacci number

# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fib(n-1) + fib(n-2)
#
# for n in range(1, 11):
#     print(n, fib(n))

# Q-4
# ENter a chr print ASCII Value of character

# def charvalue(char):
#     return ord(char)
#
# print(charvalue('b'))

# Q-5 Write a program for Array Rotation
# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
# 1 2 3 4 5 6 7
#
# Rotation by 2:
# 3 4 5 6 7 1 2

# def rotate(arr, rotateBy):
#     # print(arr)
#     chopFrontBy = arr[rotateBy:]
#     # print(chopFrontBy)
#     takeFrontBy = arr[:rotateBy:]
#     # print(takeFrontBy)
#     combine = chopFrontBy+takeFrontBy
#     return combine
#
# arr = [1,2,3,4,5,6,7]
#
# print(rotate(arr,2))

# Q-6 Write a program to Split the array and add the first part to the end
# 1 2 3 4 5 6
# 3 4 5 6 1 2

# def splitarray(array,splitby):
#     chopFrontBy = array[splitby:]
#     takeFrontBy = array[:splitby:]
#     combine = chopFrontBy+takeFrontBy
#     return combine
#
# array = [1,2,3,4,5,6]
# print(splitarray(array,3))

# Q-7 Write a program to check if given array is Monotonic
# Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone
# decreasing if for all i <= j, A[i] >= A[j]. Return “True” if the given array A is monotonic
# else return “False” (without quotes).
#
# Examples:
# Input : 6 5 4 4
# Output : true
#
# Input : 5 15 20 10
# Output : false

# def mono(arrayi, arrayj):
#     if arrayi[0] < arrayj


array = [6,5,4,4]
mono(array)