# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def move(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            
            if not inBound(row, col):
                return 0
            
            if (row + 1, col) not in cache:
                cache[(row + 1, col)] = move(row + 1, col)
                
            if (row, col + 1) not in cache:
                cache[(row, col + 1)] = move(row, col + 1)
                
            return cache[row + 1, col] + cache[row, col + 1]
            
        inBound = lambda r, c : 0 <= r < m and 0 <= c < n
        cache = {}
        return move(0, 0)
    
