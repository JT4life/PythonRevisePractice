import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
zero = 0
positiveList = []
negativeList = []

try:
    n = int(input())  # the number of temperatures to analyse
    while n == 0:
        print("0")
        break
    else:
        temps = input().split()
        if not temps:
            print("0")
        else:
            for i in temps:
                # t: a temperature expressed as an integer ranging from -273 to 5526
                t = int(i)
                if t > zero:
                    positiveList.append(t)
                    positiveList.sort()
                else:
                    negativeList.append(abs(t))
                    negativeList.sort()
        if not positiveList:
            print(-abs(negativeList[0]))
        elif not negativeList:
            print(positiveList[0])
        elif positiveList[0] <= negativeList[0]:
            print(positiveList[0])
        else:
            print(-abs(negativeList[0]))
except:
    print(sys.exc_info())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
# print(positiveList)
# print(negativeList)
# print("result")
