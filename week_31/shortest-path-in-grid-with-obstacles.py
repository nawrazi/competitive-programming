# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[r])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        heap = [(0, 0, 0, 0)]
        best = defaultdict(lambda : (inf, inf))
        
        while heap:
            steps, removed, row, col = heappop(heap)
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return steps
            
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c):
                    continue
                nex_rem = removed + grid[r][c]
                if nex_rem > k:
                    continue
                nex_steps = steps + 1
                if nex_steps < best[(r, c)][0] or nex_rem < best[(r, c)][1]:
                    heappush(heap, (nex_steps, nex_rem, r, c))
                    best[(r, c)] = (min(nex_steps, best[(r, c)][0]), min(nex_rem, best[(r, c)][1]))
                    
        return -1
    
