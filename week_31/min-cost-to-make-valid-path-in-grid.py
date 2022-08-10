# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[r])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        graph = defaultdict(list)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                cell = grid[r][c]
                for i, (x, y) in enumerate(directions):
                    _row, _col = r + x, c + y
                    if not inBound(_row, _col):
                        continue
                    if cell == i + 1:
                        graph[(r, c)].append((0, _row, _col))
                    else:
                        graph[(r, c)].append((1, _row, _col))
                        
        heap = [(0, 0, 0)]
        best = {}
        while heap:
            cur_cost, row, col = heappop(heap)
            
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return cur_cost
            
            for cost, r, c in graph[(row, col)]:
                nex_cost = cost + cur_cost
                if (r, c) not in best or nex_cost < best[(r, c)]:
                    heappush(heap, (nex_cost, r, c))
                    best[(r, c)] = nex_cost
                    
