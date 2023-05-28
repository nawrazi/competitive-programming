# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        top = Counter()
        current = defaultdict(set)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                top[(r, c)] = len(current[r-c])
                current[r-c].add(grid[r][c])
        
        bot = Counter()
        current = defaultdict(set)
        for r in range(len(grid)-1, -1, -1):
            for c in range(len(grid[0])-1, -1, -1):
                bot[(r, c)] = len(current[r-c])
                current[r-c].add(grid[r][c])
        
        ans = [[0] * len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans[r][c] = abs(top[(r, c)] - bot[(r, c)])
        
        return ans
    
