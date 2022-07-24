# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r, row in enumerate(matrix):
            c = bisect_left(row, target)
            if c < len(row) and matrix[r][c] == target:
                return True
            
        return False
    
