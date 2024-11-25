"""
HackerRank Problem: LonelyInteger
Given an array of integers, where all elements but one occur twice, find the unique element.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    counts= []
    for i in range(len(a)):
        counts.append(0)
        for j in range(len(a)):
            if a[i] == a[j]:

                counts[i] += 1

    for i in range(len(counts)):
        if counts[i] == 1:
            return a[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
