# INCOMPLETE

# https://leetcode.com/problems/pancake-sorting/submissions/

import random

def inOrder(l):
    for i in range(len(l)):
        if i != l[i]-1:
            return False
    return True

def flip(l):
    t = l
    for i in range(len(t)//2):
        t[i], t[-(i+1)] = t[-(i+1)], t[i]
    return t

def pancakeSort(arr):
    ks = []
    i=0
    while not inOrder(arr):
        k = arr.index(max(arr[i:]))
        arr = flip(arr[i:k]) + arr[:i] + arr[k:]
        i+=1
        ks.append(k)

        print(arr)
    return ks

x= [1,4,3,2,5,7,8,6]
print(pancakeSort(x))
