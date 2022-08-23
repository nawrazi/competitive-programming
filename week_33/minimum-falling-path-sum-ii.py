# https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[inf, inf], [inf, inf]] for _ in range(n)]
        dp[n-1] = sorted([[c, i] for i, c in enumerate(grid[n-1])])[:2]
        
        for r in range(n - 2, -1, -1):
            for c, cell in enumerate(grid[r]):
                grid[r][c] += dp[r+1][0][0] if c != dp[r+1][0][1] else dp[r+1][1][0]
                dp[r].append([grid[r][c], c])
                dp[r].sort()
                dp[r].pop()
                
        return min(grid[0])
    
