# https://codeforces.com/contest/1730/problem/A

from typing import Counter

t = int(input())
for _ in range(t):
    n, c = [int(n) for n in input().split()]
    p = [int(n) for n in input().split()]
    d = Counter(p)
    t = 0
    for v in d.values():
        t += min(v, c)
        
    print(t)
    
