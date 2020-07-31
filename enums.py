# 3.Use of Enums in Python

data = ['Monday', 'Tuesday', 'Wednesday', ['J', 'T', 'Z']]
enumObject = enumerate(data)
for element in enumObject:
    print(element)

class a:
    JAN, FEB, MARCH = range(3)
print(a.JAN)
print(a.FEB)