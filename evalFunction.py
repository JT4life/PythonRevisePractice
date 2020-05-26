#eval() allows us to execute a string as python code it accepts source string and returns obj

a = eval("5") #int 5
b = eval("1==1") #b is bool True
c = input("Enter an expression:") # 2**3
print(c)
print(eval(c))