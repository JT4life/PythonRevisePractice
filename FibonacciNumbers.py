# 0,1, 1,2, 3
import sys

def fib(n1=0,n2=1):
    i = 1
    f=[n1,n2]
    try:
        while i < 8:
            total = n1+n2
            f.append(total)
            n1=n2
            n2=total
            i +=1
        print(f)
    except:
        print("error ", sys.exc_info())

fib()