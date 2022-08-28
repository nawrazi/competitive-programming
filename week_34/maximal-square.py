# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        directions = [(0, 1), (1, 0), (1, 1)]
        
        @cache
        def findLength(row, col):
            if not inBound(row, col) or matrix[row][col] == '0':
                return 0
            
            max_len = inf
            for x, y in directions:
                max_len = min(max_len, findLength(row + x, col + y))
                
            return max_len + 1 if max_len != inf else 1
        
        max_len = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                max_len = max(max_len, findLength(r, c))
        
        return max_len ** 2
    
