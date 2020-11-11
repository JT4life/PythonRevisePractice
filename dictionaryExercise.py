'''
Find key from given dictionary of given value,
Taking a empty list put keys in that list if value is there and return that list
So in case Val not exist it will return empty list
'''

dic = {11:1,22:2,33:3}
val = int(input("Enter a value to check if in dictionary"))
newd = {}

for key, value in dic.items():
    if val == value:
        print(key)

print(newd)

