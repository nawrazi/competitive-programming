# https://www.hackerrank.com/challenges/insertionsort1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    num = arr[-1]

    i = n-1
    while i>=0:
        if arr[i]>num:
            print(*arr[:i], arr[i], *arr[i:-1])
            if i==0:
                print(num, *arr[:-1])

        elif arr[i]<num:
            print(*arr[:i+1], num, *arr[i+1:-1])
            break

        i-=1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
