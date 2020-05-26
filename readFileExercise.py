#3. FILE --READ FILE --- SEARCH ::
#    PYTHON | DJANGO | ORACLE KEYWORD
#---WRITE IN FILE : PYTHON : 3 | ORACLE : 5 | DJANGO : 5
import re

file1 = open ("File1.txt")
print('Opening mode:', file1.mode)
string = file1.read()
print(string)
countPython = 0
countDjango = 0
countOracle = 0

list1 = string.split(",")
print(list1)
for word in list1:
    if word.lower() == "python":
        countPython += 1
    elif word.lower() == "django":
        countDjango += 1
    elif word.lower() == "oracle":
        countOracle += 1

for word in file1:
    list1=re.split('\s',word)
for j in lst:
    if j=='PYTHON':
        cntPY+=1
    elif j=='DJANGO':
        cntD+=1
    elif j=='ORACLE':
        cntO+=1
print(countPython)
print(countDjango)
print(countOracle)

file2 = open("File1.txt", "w")
while True:
    data = input("Enter your data Python, Django, or Oracle")
    if data =="":
        break
    file2.write(data)

file1.close()
file2.close()


file=open('file98.txt','r')
lst=[]
cntPY=0
cntO=0
cntD=0
for i in file:
    lst=re.split('\s',i)
for j in lst:
    if j=='PYTHON':
        cntPY+=1
    elif j=='DJANGO':
        cntD+=1
    elif j=='ORACLE':
        cntO+=1
print('Python=',cntPY)
print('Django=',cntD)
print('Oracle=',cntO)
file.close()