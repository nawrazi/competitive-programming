# https://leetcode.com/problems/bricks-falling-when-hit/description/

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        parents = {(r, c): (r, c) for r in range(m) for c in range(n)}
        attached = {(r, c): r == 0 for r in range(m) for c in range(n)}
        size = {(r, c): 1 for r in range(m) for c in range(n)}
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def find(cell):
            if parents[cell] == cell:
                return cell
            parents[cell] = find(parents[cell])
            return parents[cell]
        
        def union(cell1, cell2):
            parent1, parent2 = find(cell1), find(cell2)
            
            if size[parent1] < size[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                attached[parent1] = attached[parent1] or attached[parent2]
                size[parent1] += size[parent2]
                parents[parent2] = parent1
                
        erased = set()
        for row, col in hits:
            if grid[row][col]:
                erased.add((row, col))
                grid[row][col] = 0
                
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    for x, y in directions:
                        nr, nc = row + x, col + y
                        if inBound(nr, nc) and grid[nr][nc]:
                            union((row, col), (nr, nc))
                            
        result = []
        for row, col in reversed(hits):
            if (row, col) not in erased:
                result.append(0)
                continue
                
            att = row == 0
            hang = 0
            seen = set()
            for x, y in directions:
                nr, nc = row + x, col + y
                if inBound(nr, nc) and grid[nr][nc]:
                    par = find((nr, nc))
                    if attached[par]:
                        att = True
                    elif par not in seen:
                        hang += size[par]
                        seen.add(par)
                        
            if att:
                result.append(hang)
            else:
                result.append(0)
                
            grid[row][col] = 1
            for x, y in directions:
                nr, nc = row + x, col + y
                if inBound(nr, nc) and grid[nr][nc]:
                    union((row, col), (nr, nc))
                    
        return reversed(result)
    
