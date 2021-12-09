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

def my_print(l):
    for n in l:
        print(n, end=' ')
    print()

def insertionSort1(n, arr):
    num = arr[-1]
    arr_truncated = arr[:-1]

    i = n-1
    while i>=0:
        if arr[i]>num:
            temp = arr_truncated
            temp.insert(i+1,temp[i])
            my_print(temp)
            temp.pop(i+1)
            if i==0:
                arr_truncated.insert(0,num)
                my_print(arr_truncated)

        elif arr[i]<num:
            arr_truncated.insert(i+1,num)
            my_print(arr_truncated)
            break

        i-=1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
