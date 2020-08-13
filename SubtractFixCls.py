from SubtractCls import subtract

def fixSubtract(function):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return function(a,b)
    return inner

sub = fixSubtract(subtract)
print(sub(10,12))
print(sub(12,10))