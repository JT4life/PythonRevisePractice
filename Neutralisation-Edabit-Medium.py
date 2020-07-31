def neutral(s1, s2):
    newList = []
    for a, b in zip(s1, s2):
        if a == '-' and b == '-':
            newList.append('-')
        elif a == '+' and b == '+':
            newList.append('+')
        else:
            newList.append('0')
    return ''.join(newList)


# s1 = '-+-+-+'
# s2 = '-+-+-+'
s1 = '--++--'
s2 = '++--++'
print(neutral(s1, s2))
#  "-+-+-+"