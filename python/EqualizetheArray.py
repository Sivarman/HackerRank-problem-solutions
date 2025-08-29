# Problem: Equalize the Array
# Link: https://www.hackerrank.com/challenges/equality-in-a-array/problem
# Description:
# Given an array of integers, determine the minimum number of deletions required
# so that all elements in the array are equal.
# You may delete any number of elements from the array.
#
# Input:
# arr - list of integers
#
# Output:
# Integer representing the minimum number of deletions required

#!/bin/python3

import math
import os
import random
import re
import sys

def equalizeArray(arr):
    d, e = 0, 0
    a = {i: arr.count(i) for i in set(arr)}
    b = [v for k, v in a.items()]
    b.remove(max(b))
    
    for i in b:
        if i == 1:
            d += 1
        else:
            e += i
    return d + e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
