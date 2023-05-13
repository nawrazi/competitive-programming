# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parents = {(r, c): (r, c) for r in range(1, row+1) for c in range(1, col+1)}
        isBorder = {(r, c): [r == 1, r == row] for r in range(1, row+1) for c in range(1, col+1)}
        
        def find(cell):
            if parents[cell] == cell:
                return cell
            parents[cell] = find(parents[cell])
            return parents[cell]
        
        def union(cell1, cell2):
            parent1, parent2 = find(cell1), find(cell2)
            
            if parent1 != parent2:
                isBorder[parent1][0] = isBorder[parent1][0] or isBorder[parent2][0]
                isBorder[parent1][1] = isBorder[parent1][1] or isBorder[parent2][1]
                parents[parent2] = parent1
                
            return all(isBorder[parent1])
        
        water = set(map(tuple, cells))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inBound = lambda r, c: 1 <= r <= row and 1 <= c <= col
        
        for day, (r, c) in enumerate(reversed(cells), 1):
            water.remove((r, c))
            for x, y in directions:
                nr, nc = r + x, c + y
                if inBound(nr, nc) and (nr, nc) not in water:
                    if union((r, c), (nr, nc)):
                        return len(cells) - day
                    
