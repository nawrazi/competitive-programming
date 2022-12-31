from collections import defaultdict

rows, cols = [int(i) for i in input().split()]
grid = []
for _ in range(rows):
    grid.append(list(input()))
    
rowc = [defaultdict(int) for _ in range(rows)]
colc = [defaultdict(int) for _ in range(cols)]

for r in range(rows):
    for c in range(cols):
        cell = grid[r][c]
        rowc[r][cell] += 1
        colc[c][cell] += 1
        
ans = []
for r in range(rows):
    for c in range(cols):
        cell = grid[r][c]
        if rowc[r][cell] == 1 and colc[c][cell] == 1:
            ans.append(cell)
            
print(''.join(ans))
