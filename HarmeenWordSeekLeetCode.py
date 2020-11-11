# Given a grid of letters find the words in the grid. The letters can be in straight sequence in any
# of the 8 directions from the first character of the word. All words might not be in the grid. Print
# the word and the start row and column position for each word that is found. For words that
# are not found, print -1 for both the row and column position. All indices start from 0

# The accepted solution should have the lowest complexity. You should iterate over the
# grid of chars only once, not once per word, if there are 'n' words given, don't parse
# through the grid 'n' times.
#
# The input words are sorted alphabetically, the output words should also be sorted.
#
# Sample input - Here is a 4x4 grid of letters as sample input. The grid is followed by
# the words to find after a blank line. All chars will be in upper case.
#
# ABCD
# PRAT
# KITA
# ANDY
#
# ANDY
# CAT
# DOG
#
# Sample Output:
# ANDY 3 0
# CAT 0 2
# DOG -1 -1

grid = [
    ['A','B','C','D'],
    ['P','R','A','T'],
    ['K','I','T','A'],
    ['A','N','D','Y'],
]

