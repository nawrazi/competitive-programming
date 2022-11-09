# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        islandSizes = {}
        
        def searchIslands(row, col, island):
            q = deque([(row, col)])
            grid[row][col] = island
            size = 0
            
            while q:
                row, col = q.popleft()
                size += 1
                for x, y in directions:
                    nr, nc = row + x, col + y
                    if inBound(nr, nc) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = island
                        
            islandSizes[island] = size
        
        def searchWater(row, col):
            counted = {0}
            size = 1
            
            for x, y in directions:
                nr, nc = row + x, col + y
                if inBound(nr, nc) and grid[nr][nc] not in counted:
                    size += islandSizes[grid[nr][nc]]
                    counted.add(grid[nr][nc])
                    
            return size
        
        island = 2
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 1:
                    searchIslands(row, col, island)
                    island += 1
                    
        if not islandSizes:
            return 1
        
        max_island = max(islandSizes.values())
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 0:
                    size = searchWater(row, col)
                    max_island = max(max_island, size)
                    
        return max_island
    
