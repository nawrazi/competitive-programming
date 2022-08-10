# https://codeforces.com/group/KIrM1Owd8u/contest/266722/problem/C

import heapq

_ = input()
nums = [int(i) for i in input().split()]

heap = [-num for num in nums]
heapq.heapify(heap)
used = set(nums)
ans = []

while heap:
    num = -heapq.heappop(heap)
    cur = num
    while cur > 0 and cur in used:
        cur //= 2
    if cur == 0:
        ans.append(num)
    else:
        used.add(cur)
        heapq.heappush(heap, -cur)

print(*ans)
