#!/bin/python3
import math
import os
import random
import re
import sys


def multiply(a, b, bound):
    if a * b <= bound:
        return a*b
    if a*b > bound:
        raise ValueError(f'multiplication of {a} and {b} with bound {bound} not possible')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for _ in range(q):
        a, b, bound = list(map(int, input().split()))
        try:
            res = multiply(a, b, bound)
            fptr.write("%d\n" % res)
        except ValueError as e:
            fptr.write("%s\n" % e)
    fptr.close()
