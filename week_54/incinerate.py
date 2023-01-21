# https://codeforces.com/gym/421768/problem/D

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
    n, k = [int(i) for i in input().split()]
    health = [int(i) for i in input().split()]
    power = [int(i) for i in input().split()]
    stats = []
    
    for i in range(n):
        stats.append((health[i], power[i]))
        
    stats.sort()
    for i in range(n):
        health[i] = stats[i][0]
        power[i] = stats[i][1]
        
    weakest = [0 for _ in range(n)]
    cur = float('inf')
    for i in range(n - 1, -1, -1):
        cur = min(cur, power[i])
        weakest[i] = cur
        
    last = 0
    while True:
        target = k + last
        pos = search(health, target) + 1
        last = target
        if pos >= n:
            print('YES')
            break
            
        k -= weakest[pos]
        
        if k <= 0:
            print('NO')
            break
            
