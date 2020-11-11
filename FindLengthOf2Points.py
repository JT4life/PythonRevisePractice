import math
'''
Write a function that takes coordinates of two points on a 
two-dimensional plane and returns the length of the line 
segment connecting those two points.

Examples
line_length([15, 7], [22, 11]) ➞ 8.06
line_length([0, 0], [0, 0]) ➞ 0
line_length([0, 0], [1, 1]) ➞ 1.41
'''

def line_length(dot1, dot2):  # ([15, 7], [22, 11])
    x = dot1[0], dot2[0]  # 15,22
    y = dot1[1], dot2[1]  # 7,11
    xTotal = x[0] - x[1]  # 37
    yTotal = y[0] - y[1]  # 18

    c = (xTotal) ** 2 + (yTotal) ** 2
    print(c)
    cTotal = math.sqrt(c)
    return round(cTotal,2)

dot1 = [15, 7]
dot2 = [22, 11]
print(line_length(dot1, dot2))