# https://codeforces.com/gym/411140/problem/D

from functools import lru_cache

@lru_cache(None)
def getWays(current, found):
    if current > n:
        return 0
    
    if current == n:
        return 1 if found else 0
    
    ways = 0
    for i in range(1, k + 1):
        ways += getWays(current + i, found or i >= d)
        
    return ways

n, k, d = [int(i) for i in input().split()]
mod = pow(10, 9) + 7
print(getWays(0, False) % mod)
