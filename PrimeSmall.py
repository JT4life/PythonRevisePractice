def primeSmall(num):
    prime = [True for i in range(num+1)]
    p = 2

    while (p * p <= num):
        #if prime[p] is not changed then it is prime
        if (prime[p] == True):
            #update all multiples of p
            for i in range(p*2, num+1, p):
                prime[i] = False

        p +=1
    prime[0] = False
    prime[1] = False
    #printing all prime nums
    for p in range(num+1):
        if prime[p]:
            print(p)

primeSmall(30)