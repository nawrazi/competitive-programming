# https://codeforces.com/contest/1676/problem/D

from collections import defaultdict

for _ in range(int(input())):
    rows, cols = [int(i) for i in input().split()]
    grid = []
    for _ in range(rows):
        grid.append([int(i) for i in input().split()])
        
    diag = defaultdict(int)
    anti = defaultdict(int)
    
    for r in range(rows):
        for c in range(cols):
            diag[r + c] += grid[r][c]
            anti[c - r] += grid[r][c]
            
    m = 0
    for r in range(rows):
        for c in range(cols):
            m = max(m, diag[r + c] + anti[c - r] - grid[r][c])
            
    print(m)
    
