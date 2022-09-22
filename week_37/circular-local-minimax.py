# https://codeforces.com/contest/1685/problem/A

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    nums = deque(sorted(int(n) for n in input().split()))
    if n % 2 == 1:
        print('NO')
        continue
    order = []
    poss = True
    j = n // 2
    for i in range(n // 2):
        if (order and nums[i] == order[-1]) or nums[i] == nums[j]:
            poss = False
            break
        order.append(nums[i])
        order.append(nums[j])
        j += 1

    if poss:
        print('YES')
        print(*order)
    else:
        print('NO')
        
