def binary_search(arr, val, start, end):
    #first determine if we insert before or after the left boundary
    #imagine [0] is the last step of the binary search and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    #this occus if we're moving beyond lefts boundary
    if start > end:
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr,val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

arr = [3,52,12,25,31,6]
print("sorted array")
print(insertion_sort(arr))