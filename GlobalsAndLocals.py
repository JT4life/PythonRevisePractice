# Global and local variables

x = 1000

def display():
    global x # Overrides the global variable
    x = 2000
    n = 9000
    print(n)
    print(x)

display()
print(x)
