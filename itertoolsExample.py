from itertools import product

# product ( takes iterables, repeat=1)

for i in product('ab', range(3)):
    print(i)

for i in product((0,1),(0,1),(0,1)):
    print(i)

for i in product("A", repeat=3):
    print(i)