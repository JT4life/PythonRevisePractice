#Remember functions are objects can be passed through parameters
def f1():
    print("Call f1")

def f2(f):
    f() #calling function

# f2(f1)
# print(f1)

#Wrapper Functions

def func1(func):
    def wrapper(*args, **kwargs): #func within function, calls func then ends
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper
@func1
def f(a, b=9):
    print(a,b)

# func1(f)()
# print(func1(f))

# x = func1(f)
# x()

f('hi')

@func1
def add(x,y):
    return x+y

print(add(4,5))