# Write a function named get3coordinates that collects 3
# coordinates from users, return the 3 coordinates.
# Write a function named calculate_length that accepts 2 coordinates,
# and calculates and returns the length of the 2 coordinates. Write a
# function named calculate3lengths that accepts 3 coordinates, use the above
# calculate_length function to obtain the 3 lengths among the 3 coordinates,
# return the 3 lengths.•Write a function named sort3numbers that accepts 3 numbers,
# return the 3 numbers in ascending order.•Print the 3 lengths in ascending order.

def get3coordinates(one, two, three):
    return one, two, three

def calcLength(one, two):
    return one+two

def calc3(cord1, cord2, cord3):
    oneTwo = calcLength(cord1, cord2)
    twoThree = calcLength(cord2, cord3)
    threeOne = calcLength(cord3, cord1)
    return oneTwo, twoThree, threeOne

def sort3nums(one, two, three):
    lst = [one,two,three]
    lst.sort()
    print(lst)

# print(get3coordinates(2,4,6))
# print(calcLength(4,5))
# print(calc3(5,3,6))
# sort3nums(7,4,9)

# Write a function that returns the reverse of a string. Use 'for' loop
lst = []
def reverseString(word=[]):
    for letters in word:
        lst.insert(0,letters)
    print(lst)

reverseString("Joshua")

stringWord = "Youtube"
stringReverse = stringWord[::-1]
print(stringReverse)