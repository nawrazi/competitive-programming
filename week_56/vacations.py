# https://codeforces.com/gym/425420/problem/C

from functools import lru_cache

@lru_cache(None)
def minTime(idx, last):
    if idx >= n:
        return 0
    
    if arr[idx] == 0:
        return 1 + minTime(idx + 1, -1)
    elif arr[idx] == 1:
        if last == 0:
            return 1 + minTime(idx + 1, -1)
        else:
            return minTime(idx + 1, 0)
    elif arr[idx] == 2:
        if last == 1:
            return 1 + minTime(idx + 1, -1)
        else:
            return minTime(idx + 1, 1)
    else:
        if last == 0:
            return min(1 + minTime(idx + 1, 0), minTime(idx + 1, 1))
        elif last == 1:
            return min(1 + minTime(idx + 1, 1), minTime(idx + 1, 0))
        else:
            return min(minTime(idx + 1, 1), minTime(idx + 1, 0))
        
n = int(input())
arr = [int(n) for n in input().split()]
print(minTime(0, -1))
