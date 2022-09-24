# https://codeforces.com/problemset/problem/1734/A

t = int(input())
for _ in range(t):
    n = int(input())
    nums = sorted(int(n) for n in input().split())
    diff = []
    for i in range(1, n):
        diff.append(nums[i] - nums[i - 1])

    ops = float('inf')
    for i in range(1, len(diff)):
        ops = min(ops, diff[i] + diff[i - 1])
    
    print(ops)
    
