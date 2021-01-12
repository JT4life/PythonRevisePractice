import re

# 1.)Write a program to  validate the dates from the following lines.
# # R21331.006.000.012.047.1704111352
# # W2344234.006.000.033.000.1713322001

'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('\r')