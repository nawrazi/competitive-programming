# https://codeforces.com/gym/424201/problem/A

from math import ceil, floor

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    mn, mx = -float('inf'), float('inf')
    
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            continue
        elif arr[i] < arr[i - 1]:
            cmn = ceil((arr[i] + arr[i - 1]) / 2)
            mn = max(cmn, mn)
        else:
            cmx = floor((arr[i] + arr[i - 1]) / 2)
            mx = min(mx, cmx)
            
    if mx >= mn:
        print(mx if mx != float('inf') else (mn if mn != -float('inf') else 0))
    else:
        print(-1)
        
