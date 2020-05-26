list2 = [1,2,"3",3]
list3 = []
list4 = []
for i in list2:
    if i.isdigit():
        list3.append(i)
    else:
        list4.append(i)

print(list3)
print(list4)