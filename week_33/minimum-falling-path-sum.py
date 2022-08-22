# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        directions = [(1,-1), (1,0), (1,1)]
        inBound = lambda r, c: 0 <= r < n and 0 <= c < n
        
        dp = [[inf for _ in range(n)] for _ in range(n - 1)]
        dp.append(matrix[-1][:])
        
        for r in range(n - 2, -1, -1):
            for c in range(n):
                for x, y in directions:
                    nr, nc = r + x, c + y
                    if not inBound(nr, nc):
                        continue
                    dp[r][c] = min(dp[r][c], matrix[r][c] + dp[nr][nc])
                    
        return min(dp[0])
    
