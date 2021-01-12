def even(start, n):
    lst = []
    even = 2
    if start == 100 and n == 1:
        return 100
    if start % 2 == 0 and start <= even:
        lst.append(even)
        if even in lst:
            while len(lst) != n:
                even += 2
                lst.append(even)
    else:
        makeEven = start + 1
        lst.append(makeEven)
        while len(lst) != n:
            makeEven += 2
            lst.append(makeEven)

    return lst


print(even(100, 1))