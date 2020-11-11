# map takes in (function, iterables)

def square(n):
    return n*n

list1 = [1,2,3,4]

res = map(square, list1)
print(list(res))

# Filters out the data you don't need, returns iterator yielding
# those items of iterable for which function(item) is true
# If function is None return the items that are true
# filter(function or None, iterable)
data = [1.2,2.2,2.3,4.2]

x = filter(lambda x : x > 3, data)
print(list(x))


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)


# lambda is a python keyword that says what follows is the anonymous function
# lambda follows by 0 or more inputs then a colon: then single expression which is the return value
def f(x):
    return 3*x+1
print(f(2))

g = lambda x: 3*x+1
print(g(2))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name(" joshua", "  thao "))

# lambda without a name
scifi_auth = ["abby gold", "jes alba vins", "robert half"]
scifi_auth.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_auth)
