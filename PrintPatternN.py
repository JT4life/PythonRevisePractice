def printPat(n):
    for i in reversed(range(1,n+1)): #i=3 since its reversed 3 first
        for j in reversed(range(1,n+1)): #j=3
            print('{} '.format(str(j))*i,end ="") #will print 333 first, then 222
        print('$',end ="")

n=3
printPat(3)