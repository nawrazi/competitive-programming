# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen = defaultdict(int)
        for row in grid:
            seen[tuple(row)] += 1
            
        pairs = 0
        for c in range(len(grid[0])):
            col = [row[c] for row in grid]
            pairs += seen[tuple(col)]
            
        return pairs
    
