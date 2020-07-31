#Quick sorts it in ascending or descending order
#Take 1 item and make it pivot point, its just the number we are going to compare all others off of
#If its higher it goes to the right list if lower left list
#Then take the pivot points of the 2 lists and compare it

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
            
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,2,1,9,8]))