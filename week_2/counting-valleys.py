# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    level = 0
    valleys = 0

    n= len(path)

    for i in range(n):
        if path[i]=='U':
            level+=1

            if level==0:
                valleys+=1
        else:
            level-=1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
