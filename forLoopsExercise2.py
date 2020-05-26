# Marks
markList = []
totalOfMarks = int(input("Enter marks between 0-100 or type '00' to exit"))
while totalOfMarks != 00:
    markList.append(totalOfMarks)
    totalOfMarks = int(input("Enter marks between 0-100 or type '00' to exit"))
print(markList)
passing = 60
peoplePassed = 0
peopleFailed = 0
for i in markList:
    if i >= passing:
        peoplePassed += 1

    else:
        peopleFailed += 1

print("people who passed", peoplePassed)
print("people failed", peopleFailed)
print("lowest mark/scored = ", min(markList))
print("highest mark/scored = ", max(markList))