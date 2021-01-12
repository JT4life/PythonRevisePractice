my_list = ['apples', 'pears', 'oranges', 'fruits']

# enumerate

for x, element in enumerate(my_list):
    print(x, element)

# 1 way
# count = 0
# for element in my_list:
#     print(element)
#     if count == 1:
#         print("Count is 1")
#     count+=1
#
# # second way
# for x in range(len(my_list)):
#     print(my_list[x])
#     if x == 1:
#         print("x is 1")