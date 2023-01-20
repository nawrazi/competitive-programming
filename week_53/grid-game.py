# https://leetcode.com/problems/grid-game/description/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = [[0], [0]]
        for row in range(2):
            for col in range(len(grid[row])):
                prefix[row].append(grid[row][col] + prefix[row][-1])
                
        min_points = inf
        for col in range(1, len(prefix[0])):
            top = prefix[0][-1] - prefix[0][col]
            bottom = prefix[1][col - 1]
            min_points = min(min_points, max(top, bottom))
            
        return min_points
    
