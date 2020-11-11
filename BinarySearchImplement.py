# In binary search we take a sorted list of elements and start looking for an
# element at the middle of the list. If the search value matches with the middle
# value in the list we complete the search. Otherwise we eliminate half of the list
# of elements by choosing whether to process with the right or left half of the list
# depending on the value of the item searched. This is possible as the list is sorted and
# it is much quicker than linear search. Here we divide the given list and conquer by choosing
# the proper half of the list. We repeat this approach till we find the element
# or conclude about it's absence in the list.

def binary_search(list, value):
    start = 0
    end = len(list)-1

    #Find mid
    while start <= end:
        mid = (start+end) // 2

        if list[mid] == value:
            return mid
        #compare the value the mid most value
        if value > list[mid]:
            start = mid+1
        else:
            end = mid-1

    if start > end:
        return None

list1 = [1,2,3,44,55]

print("your value is located at index ",binary_search(list1,3))
print("your value is located at index ",binary_search(list1,1))
print("your value is located at index ",binary_search(list1,555))