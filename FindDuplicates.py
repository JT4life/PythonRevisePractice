def dups(lst):
    seen = set()
    uniq = []
    for x in lst:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
    return sorted(uniq)


lst = [1, 1, 4, 3, 2]

print(dups(lst))