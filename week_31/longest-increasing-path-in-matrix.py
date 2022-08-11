# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def search(row, col):
            longest = 1
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                r, c = row + x, col + y
                if not inBound(r, c) or matrix[row][col] >= matrix[r][c]:
                    continue
                longest = max(longest, search(r, c) + 1)
            return longest
        
        inBound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[r])
        longest = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                longest = max(longest, search(r, c))
                
        return longest
    
