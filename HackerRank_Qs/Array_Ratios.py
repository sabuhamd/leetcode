"""
HackerRank Problem: Array Ratios
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    zer = 0
    neg = 0
    pos = 0
    for i in range(n):
        if arr[i] == 0:
            zer += 1
        elif arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
    posrat = pos/n
    zerrat = zer/n
    negrat = neg/n
    print(f"{posrat:.6f}")
    print(f"{negrat:.6f}")
    print(f"{zerrat:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
