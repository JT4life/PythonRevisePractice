def fib(n):
    v1, v2 = 0, 1
    while v1 < n:
        print(v1, end=' ')
        v1, v2 = v2, v1 + v2
    print()


def bar(n):
    res = []
    v1, v2 = 0, 1
    while v1 < n:
        res.append(v1)
        v1, v2 = v2, v1 + v2
    return res
