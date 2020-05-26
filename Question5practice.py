# make c = 4
slist = [4,7,[2,4,6,8]]
c = 0
for i in range(3):
    if type(slist[i]) == list:
        # for j in slist:
        # for j in [2,4,5,10]:
        for j in slist[i]:
        # for j in range(3):
            if j % 2 == 0:
                c+=1
            else:
                c-=1
print(c)