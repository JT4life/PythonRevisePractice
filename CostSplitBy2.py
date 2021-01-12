from itertools import product

def f(cost, high, low):
    # Split the cost between 2 people, the lowest amount a person can
    # contribute is the low and the highest is the high, how many
    # different ways can the cost be split?
    counter = 0
    lst = []
    for i in range(2, 4 + 1):
        lst.append(i)
    for pair in product(lst, repeat=2):
        if sum(pair) == 5:
            counter += 1
    return counter


cost = 5
low = 2
high = 4

print(f(cost, high, low))