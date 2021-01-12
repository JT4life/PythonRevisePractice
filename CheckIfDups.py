# def checkIfDups(lst):
#     if len(lst) == len(set(lst)):
#         return False
#     else:
#         return True
#
# lst = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
# result = checkIfDups(lst)
# if result:
#     print('Yes, list contains duplicates')
# else:
#     print('No duplicates found in list')

# def checkIfDuplicates_2(listOfElems):
#     ''' Check if given list contains any duplicates '''
#     setOfElems = set()
#     dups = []
#     for elem in listOfElems:
#         if elem in setOfElems:
#             dups.append(elem)
#         else:
#             setOfElems.add(elem)
#     return sorted(set(dups))
#
# # listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
# listOfElems = [6,3,3,3,5,1,1,2,4]
# print(checkIfDuplicates_2(listOfElems))



# def checkDups3(listOfElems):
#     new_list = []
#     for elem in listOfElems:
#         if listOfElems.count(elem) > 1:
#             new_list.append(elem)
#     return sorted(set(new_list))
#
# # listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
# listOfElems = [6,5,1,1,2,3,3,3,4]
#
# print(checkDups3(listOfElems))