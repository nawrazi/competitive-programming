# https://codeforces.com/contest/1676/problem/F

from collections import Counter

def solve(nums, k):
    c = Counter(nums)
    counts = list(filter(lambda x: c[x] >= k, [k for k, v in c.items()]))
    
    counts.sort()
    longest = 0
    last = 0
    vals = []
    for i in range(1, len(counts) + 1):
        if i == len(counts) or counts[i] - counts[i-1] != 1:
            if i - last > longest:
                longest = i - last
                vals = [counts[last], counts[i-1]]
            last = i

    if vals:
        print(*vals)
    else:
        print(-1)

    
t = int(input())
for _ in range(t):
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    solve(nums, k)
    
