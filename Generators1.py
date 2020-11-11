import sys

#we have a finite amount of memory, since we are limited we need generators

#0 squared up to n
# x = [i**2 for i in range(100000)]
#
# for el in x:
#     print(el)
#
# for i in range(100000): #same as above code
#     print(i**2)

#Generator class
# class Gen:
#     def __init__(self, n):
#         self.n = n
#         self.last = 0
#
#     def __next__(self):
#         return self.next()
#
#     def next(self):
#         if self.last == self.n:
#             raise StopIteration()
#
#         rv = self.last ** 2
#         self.last += 1
#         return rv
#
# g=Gen(100)
#
#
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

# will run faster because it is not being stored in a list, all we are doing is keeping track of the next generator value
# we only store the last value generator and generator the next, think of yield as a pause as return is like a stop
def gen(n):
    for i in range(n):
        yield i**2

g = gen(100000)
# for i in g:
#     print(i)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # will stop iteration of there is no next iteration

y = [i**2 for i in range(1000)]

print(sys.getsizeof(y)) # in bytes
print(sys.getsizeof(g))