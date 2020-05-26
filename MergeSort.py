# Take input from user of unsorted list
# first take a list and then divide the list

def mergeSort(listA):
    if len(listA) > 1:  # if length has less than 1 element we stop
        mid = len(listA) // 2
        leftSublist = listA[:mid]  # begin index to middle
        rightSublist = listA[mid:]
        # use recursive to divide the sublist further
        mergeSort(leftSublist)
        mergeSort(rightSublist)

        i = 0
        j = 0
        k = 0  # the variable used to store the sorted list

        # i is the index of left list and will always be smaller than len list
        while i < len(leftSublist) and j < len(rightSublist) :
            if leftSublist[i] < rightSublist[j]:
                listA[k] = leftSublist[i]
                i = i + 1
                k = k + 1
            else:
                listA[k] = rightSublist[j]
                j = j + 1
                k = k + 1
        # in case any other elements are left out of loop
        while i < len(leftSublist):
            listA[k] = leftSublist[i]
            i = i + 1
            k = k + 1
        while j < len(rightSublist):
            listA[k] = rightSublist[j]
            j = j + 1
            k = k + 1


listSize = int(input("Enter a number to create the size of elements in your list"))
listA = [int(input()) for x in range(listSize)]
mergeSort(listA)
print("The sorted list is: ", listA)


