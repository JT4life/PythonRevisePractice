age = 0
while age >= 0:
    age = int(input("Enter your age or type a negative number to exit"))
    if age < 18:
        print("Minor", age)
    elif age >= 18 and age < 60:
        print("Adult", age)
    else:
        print("Senior", age)

