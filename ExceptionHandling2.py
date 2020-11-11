import sys

# try:
#     n = int(input("Enter a number"))
#     m = int(input("Enter a number"))
#     print(n/m)
# except Exception as e:
#     print("error is ",e)
#     print(sys.exc_info())
# else:
#     print("else will run if there is no exception")
# finally:
#     print("finally always run")

# Nested Try

try:
    a = int(input("Enter number"))
    print(a)
    if a > 100:
        raise NameError("Value > not allowed")
except:
    print("Not a proper value")