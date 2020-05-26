# 2. LIST ----NUMBER / STRING ---->2 SEPRATE LIST

list1 = [1, 2, "a", "b"]

# l1 = list1[:2]
# l2 = list1[2:]
# print(l1)
# print(l2)
listNumber = []
listString = []
for value in list1:
    if isinstance(value, int):
        listNumber.append(value)
    else:
        listString.append(value)

print(listNumber)
print(listString)