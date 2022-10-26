# https://codeforces.com/gym/406242/problem/B

from math import factorial
from typing import Counter

def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

for _ in range(int(input())):
    input()
    nums = [int(i) for i in input().split()]
    diffs = []
    for i, num in enumerate(nums):
        diffs.append(num - (i + 1))
        
    cnt = Counter(diffs)
    ans = 0
    for c in cnt.values():
        if c > 1:
            ans += combination(c, 2)
            
    print(ans)
    
