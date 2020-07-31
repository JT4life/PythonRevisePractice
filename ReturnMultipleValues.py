# 4. Return multiple values from functions
def returnMulti():
    yield 1
    yield 2

def a():
    return 4, 5, 6, 7
p, q, r, s = a()
print(p, q, r, s)