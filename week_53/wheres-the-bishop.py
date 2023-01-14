# https://codeforces.com/contest/1692/problem/C

def solve():
    grid = []
    for _ in range(8):
        grid.append(list(input()))
        
    directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    
    for r in range(1, 7):
        for c in range(1, 7):
            if grid[r][c] == '.':
                continue
                
            for x, y in directions:
                nr, nc = r + x, c + y
                if grid[nr][nc] == '.':
                    break
            else:
                return (r + 1, c + 1)
            
t = int(input())
for _ in range(t):
    input()
    print(*solve())
    
