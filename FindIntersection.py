'''
goal is to return a comma separated string containing the numbers that occur in elements of strarr in sorted order
if there is no intersection return the string
'''
def FindIntersection(strArr):
    a, b = strArr
    int_a = []
    int_b = []
    both = ""
    list_a = [x.strip() for x in a.split(",")]
    list_b = [x.strip() for x in b.split(",")]
    for ele in list_a:
        int_a.append(ele)
    for ele in list_b:
        int_b.append(ele)
    for i in list_a:
        if i in list_b:
            both = both+i+","
    return both[:-1]

strArr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

# keep this function call here
print(FindIntersection(strArr))