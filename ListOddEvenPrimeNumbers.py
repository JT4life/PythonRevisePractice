l1 = [1,1,2,2,3,4,5,6,7,8,9]

def even(list):
    even = []
    for nums in list:
        if nums % 2 == 0:
            even.append(nums)
    return even

# print(even(l1))
evenList = even(l1)

def odd(list):
    odd = []
    for nums in list:
        if nums % 2 != 0:
            odd.append(nums)
    return odd

# print(odd(l1))
oddList = odd(l1)

def prime(list):
    prime = []
    for nums in list:
        if nums > 1:
            for i in range(2,nums):
                if nums % i == 0:
                    # print("not prime ", nums)
                    break
            else:
                prime.append(nums)
                # print(nums, "is prime ")
        else:
            # print("not prime ", nums)
            pass
    return prime

# print(prime(l1))
primeList = prime(l1)

def removeDups(list):
    # result = []
    # for nums in list:
    #     if nums not in result:
    #         result.append(nums)
    # return result
    listIntoSet = set(list)
    return listIntoSet

print(removeDups(l1))

def appendList(even, odd, prime):
    newList = []
    while even != None and odd != None and prime != None:
        newList.append(even)
        newList.append(odd)
        newList.append(prime)
        break
    return newList

print(appendList(evenList,oddList,primeList))