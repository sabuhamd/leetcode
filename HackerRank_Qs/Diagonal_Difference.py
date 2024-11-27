"""
Hacker Rank Problem DiagonalDifference
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    prime_diag = []
    secon_diag = []

    for i in range(len(arr)):

        prime_diag.append(arr[i][i])
    prime_sum =  sum(prime_diag)
    for i in range(len(arr)):
        print(len(arr)-i)
        secon_diag.append(arr[i][len(arr) -1 - i])
    secon_sum = sum(secon_diag)
    return abs(prime_sum - secon_sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
