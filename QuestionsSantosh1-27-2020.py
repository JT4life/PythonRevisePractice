# 1. Question:
# With a given tuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a
# program to print the first half values in one line and the
# last half values in one line.

# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# def a(tuple):
#     firsthalf = tuple[:5]
#     print("first half", firsthalf)
#     secondhalf = tuple[5:]
#     print("second half", secondhalf)
#
# a(tup)

#2. Write a program to generate and print another tuple whose
# values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# def even(tup):
#     evenList = []
#     for i in tup:
#         if i % 2 == 0:
#             evenList.insert(0,i)
#     print(tuple(evenList))
#
# even(tup)

#3. Question:
# WAP that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# def words():
#     words1 = input("Enter some words separated by commas eg. you,are,here")
#     a = words1.split(",")
#     a.sort()
#     print(a, sep=",")
#
# words()

# 4 Question:
# WAP that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and
# sorting them alphanumerically. Suppose the following input is
# supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


def whitespace():
    words = input("Type in some words separated by spaces eg. hello how are you")
    split = words.split(" ")
    lst2 = []
    dups = []
    print(split)
    for word in split:
        lst2.append(word)
        for i in lst2:
            if i in split:
                dups.append(i)
        print(set(dups))

whitespace()

# 5. Question:
# A User Registration form requires the users to input username and password to register.
# Write a program to check the validity of password input by users. criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and
# will check them according to the above criteria. Passwords that match the
# criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# PXd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# PXd1234@1

def takeInput():
    userInput = input("""Please type in a password must be minimum 6-12 characters,
    must have at least 1 number 0-9, 1 capital letter, 1 special character of #$@""")

