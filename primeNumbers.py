p = 2

while p <= 100:
    is_prime = True
    for i in range (2, p):
        if p % i == 0:
            is_prime = False
            print("Not a prime number ", p)
            break
    if is_prime == True:
        print("Is a prime number ", p)
    p = p +1
