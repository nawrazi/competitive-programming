# https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = Counter()
        cols = Counter()
        servers = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (rows[row] > 1 or cols[col] > 1):
                    servers += 1
                    
        return servers
    
