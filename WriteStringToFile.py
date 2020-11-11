import re
import sys

# 1. String :"Donald Trump" ---D.Trump ---->File
#            "ABCD XYZ KBC" ---A.Xyz.KBC -->File

# def string(FullName):
#     first = FullName[:1]
#     nameSplit = FullName.split(" ")
#     final = first + "."
#     try:
#         if len(nameSplit) > 2:
#             final = final + str(nameSplit[1]) + "." + str(nameSplit[2])
#         elif len(nameSplit) > 1:
#             final = final + str(nameSplit[1])
#         file1 = open("Name.txt", "w")
#         file1.write(final)
#         file1.close()
#     except Exception as e:
#         print(e)
#
# FullName = "Donald Trump"
# print(string(FullName))

# 2. Read File ---Store Data in List (Without any special chr)

# def readFile():
#     try:
#         with open('Name.txt', 'r') as f:
#             special = [re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", file) for file in f]
#             print(special)
#         f.close()
#     except Exception as e:
#         print(e)
#
# readFile()

# 3. Copy the List in another Existing List
# def list(one, two):
#     result = two[:]+one[:]
#     return result
#
# one = [1,2,3]
# two = [4,5,6]
#
# print(list(one,two))

# 4. Remove Duplicate value from List
def dups(lst):
    seen = set()
    found = []
    for i in lst:
        if i not in seen:
            found.append(i)
            seen.add(i)
    return found

lst = [1,1,2,2,3]
print(dups(lst))

# 5. Concatinate all the values ---Write in File
def concat():
    try:
        file1 = open("Name.txt", "a") #append
        print("Opening mode:", file1.mode)
        while True:
            data = input("Enter your data: ")
            if data =="":
                break
            file1.write(data+'\n')
        file1.close()
    except Exception as e:
        print(e)

concat()