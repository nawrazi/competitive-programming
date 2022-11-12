# https://codeforces.com/gym/409730/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    skip = 2
    f = False
    while not f and skip < n:
        mn, mx = float('inf'), float('-inf')
        for i in range(n):
            if i > 0 and i % skip == 0:
                if mx - mn != skip - 1:
                    f = True
                    break
                mn, mx = float('inf'), float('-inf')
            mn = min(mn, arr[i])
            mx = max(mx, arr[i])
        skip *= 2
        
    if f:
        print(-1)
        continue
        
    swaps = 0
    reps = arr.copy()
    temp = []
    skip = 2
    f = False
    while not f and len(reps) > 1:
        for i in range(0, len(reps) - 1, 2):
            if reps[i] > reps[i+1]:
                swaps += 1
            mx = max(reps[i], reps[i+1])
            if mx % skip != 0:
                print(-1)
                f = True
                break
            temp.append(mx)
        reps = temp.copy()
        temp.clear()
        skip *= 2
        
    if not f:
        print(swaps)
        
