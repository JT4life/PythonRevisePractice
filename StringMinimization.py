#1
string = 'cabbaaabcc'

def min(string):
    left = []
    right = []
    size = len(string)//2

    left.append(string[size:])
    right.append(string[:size])
    print(left)
    print(right)




min(string)
# str1 = 'aabcccabba'
# left_str,right_str=str1[:len(str1)//2],str1[len(str1)//2:]
# while left_str[0]==right_str[-1]:
#     left_str,right_str=left_str.lstrip(left_str[0]),right_str.rstrip(right_str[-1])
# new_str=right_str+left_str
# print(new_str)

#2
# str2='cabbaaabcc'
# for char in str2:
#     str2=str2.replace(char*3,'')
# print(str2)
# print(len(str2))

#3
