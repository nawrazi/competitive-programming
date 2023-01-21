# https://codeforces.com/contest/1777/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    last = arr[0] + 1
    swaps = 0
    for a in arr:
        if a % 2 == last % 2:
            swaps += 1
        last = a
        
    print(swaps)
    
