

yourNum = int(input("Enter a number to see if its prime"))

for i in range(2, yourNum):
    if yourNum % i == 0:
        print("Not a prime number ", yourNum)
        break
else:
    print("prime", yourNum)