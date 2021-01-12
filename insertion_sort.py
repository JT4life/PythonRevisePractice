def ins_sort(lst):
    index_length = range(1, len(lst))
    for i in index_length:
        val_to_sort = lst[i]

        while lst[i-1] > val_to_sort and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i =i-1
    return lst

print(ins_sort([6,4,7,2]))

# same complexity as bubble sort but may be faster with less elements