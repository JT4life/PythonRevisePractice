# Consider the example of recording temperatures 4 times
# a day, every day. Some times the recording instrument may
# be faulty and we fail to record data. Such data for 4 days
# can be presented as a two dimensional array as below.

# Day 1 - 11 12 5 2
# Day 2 - 15 6 10
# Day 3 - 10 8 12 5
# Day 4 - 12 15 8 6

# Above data can be represented as a two dimensional array as below.

temperatures = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

# print(temperatures[0])
# print(temperatures[1][2])

# print out the entire two dimensional array we can use python for loop as shown
# below. We use end of line to print out the values in different rows.

# for r in temperatures:
#     for c in r:
#         print(c, end = " ")
#     print()

#insert values into our 2d array

temperatures.insert(2, [0,5,11,13,6])
# output
# 11 12 5 2
# 15 6 10
# 0 5 11 13 6
# 10 8 12 5
# 12 15 8 6

#update values in 2d array

temperatures[2] = [11,9]

for r in temperatures:
    for c in r:
        print(c, end = " ")
    print()

#delete values

# del temperatures[3]