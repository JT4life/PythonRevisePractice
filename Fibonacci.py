def Fibo(n):
    a = 1
    b = 0
    while a < n:
        print(a, end=" ")
        a, b = a+b, a


Fibo(9)