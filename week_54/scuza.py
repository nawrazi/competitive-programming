# https://codeforces.com/gym/421768/problem/A

from itertools import accumulate

def search(arr, target):
    left, right = 0, len(arr) - 1
    best = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            best = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return best

for _ in range(int(input())):
    n, q = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    queries = [int(i) for i in input().split()]
    
    prefix = list(accumulate(arr))
    limit = []
    cur = 0
    for a in arr:
        cur = max(cur, a)
        limit.append(cur)
        
    ans = []
    for q in queries:
        idx = search(limit, q)
        if idx < 0:
            ans.append(0)
        else:
            ans.append(prefix[idx])
    
    print(*ans)
    
