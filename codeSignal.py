#Find next prime number
def prime(n):
    next_prime = n + 1
    prime = True
    while prime == True:
        for i in range(2, next_prime):
            if next_prime%i ==0:
                prime = False
                # break
        if prime:
            return next_prime
        else:
            next_prime +=1
            if next_prime % 2 == 0:
                next_prime +=1
            prime = True
print(prime(103))