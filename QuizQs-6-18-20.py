import sys
import json
from pymongo import MongoClient
import sqlite3
import os
import numpy as np

# 1. given a list of numbers display prime numbers in another list
# and even numbers in another list in descending order

# def listOfN(lst):
#     primeList = []
#     evenList = []
#     notPrime = []
#     try:
#         for i in lst:
#             if i % 2 == 0:
#                 evenList.append(i)
#             if i == 2:
#                 primeList.append(i)
#             if i > 2:
#                 for j in range(2,i):
#                     if i % j == 0:
#                         notPrime.append(i)
#                         break
#                     else:
#                         primeList.append(i)
#                         break
#         primeList.sort(reverse=True)
#         evenList.sort(reverse=True)
#     except:
#         print(sys.exc_info())
#     print("prime nums ",primeList)
#     print("even nums ",evenList)
#     print("Not prime nums ",notPrime)
#
# lst = [1,2,3,4,5,6,7,8,9,10,11]
#
# listOfN(lst)

#2. Given a dictionary with KV convert it into json format. Then import into MongoDB

# def convertJson(dic):
#     conn = MongoClient("localhost", 27017)
#     db = conn.test.emp1
#     js = json.dumps(dic)
#     #checking
#     print(js)
#     try:
#         with open('dic.json', 'w') as f:
#             file_data = json.loads(js)
#             # print(file_data)
#             db.insert(file_data)
#             conn.close()
#     except:
#         print(sys.exc_info())
#
# dic = {1:"Josh", 2:"Harmeen", 3:"Tess", 4:"Zie"}
# convertJson(dic)


# 3. Given a string "Allen Smith Border" display A.S.Border only initials with Full LastName
# Then reverse the string Border Smith Allen. Then count numbers of characters without space
# Then count the number of words.

# def givenStr(string):
#     charsCount = 0
#     words = []
#     wordB = []
#     revers = string[::-1]
#     try:
#         for i in string:
#             while i != ' ':
#                 charsCount +=1
#                 break
#         print("character count ",charsCount)
#         numOfWords = len(string.split())
#         print("number of words ",numOfWords)
#         for i in string.split():
#             words.append(i)
#         print(words)
#         for i in words:
#             if i != words[-1]:
#                 wordB.append(i[0])
#         print('.'.join(wordB),'.',(words[-1]))
#         print(revers)
#     except:
#         print(sys.exc_info())
#
# string = "Allen Smith Border"
# givenStr(string)

# 4. Create a file sqlite (emp:empno,ename,sal)
# Read the file. Copy the data into another new file. Then remove previous file.

# def sqlite():
#     conn = sqlite3.connect("empdata.db")
#     cursor = conn.cursor()
#     cursor.execute("Drop table employee;")
#     sqlCommand = """CREATE TABLE employee(
#         empno INTEGER PRIMARY KEY,
#         ename VARCHAR(20),
#         salary INTEGER);"""
#     cursor.execute(sqlCommand)
#     empno = int(input("Enter employee number"))
#     ename = input("Enter employee name")
#     salary = int(input("Enter employee salary"))
#     cursor.execute("insert into employee (empno, ename, salary) VALUES (?,?,?)",(empno,ename,salary))
#     conn.commit()
#     print("Data Inserted!!!")
#     cursor.execute("SELECT * from employee")
#     print("fetchall:")
#     result = cursor.fetchall()
#     convertToString = str(result)
#     for r in result:
#         print(r)
#     with open('empdata.txt', 'wt') as f:
#         txt = f.write(convertToString)
#         print("emp data saved", txt)
#
# sqlite()

# 5. Array, transpose the array,  column is converted in to the row, row to column
# Display the row sum and column sum.

lst = np.array([[1,2],[3,4],[5,6]])

sumCol = lst.sum(axis=0)
print("Sum of column = ", sumCol)

sumRow = lst.sum(axis=1)
print("Sum of rows = ", sumRow)

transpose = lst.transpose()
print(transpose)