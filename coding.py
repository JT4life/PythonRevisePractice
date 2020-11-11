def arr(strA):
    lst = []
    for i in strA:

        lst.append(i)
    print(lst)

    return strA


strArr = ["(0 0)", "(3 0)", "(0 0)", "(3 2)"]

print(arr(strArr))