names = str(input("Enter everyones name at the party"))
listNames = names.split(" ")
listNames.sort()
print(listNames)

guests = []
name1 = ""

while name1 != "DONE":
    name1 = input("Enter guest name (Enter DONE if no more names) : ")
    if name1.upper() != "DONE" :
        guests.append(name1)

guests.sort()
for guest in guests:
    print(guest)