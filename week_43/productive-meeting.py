# https://codeforces.com/gym/407211/problem/C

from heapq import heappop, heappush

for _ in range(int(input())):
    input()
    nums = [int(i) for i in input().split()]
    heap = []
    
    for i, n in enumerate(nums, 1):
        if n != 0:
            heappush(heap, (-n, i))
            
    ans = []
    while len(heap) > 1:
        fir, idx1 = heappop(heap)
        sec, idx2 = heappop(heap)
        ans.append([idx1, idx2])
        
        if fir < -1:
            heappush(heap, (fir + 1, idx1))
        if sec < -1:
            heappush(heap, (sec + 1, idx2))
            
    print(len(ans))
    for a in ans:
        print(*a)
        
