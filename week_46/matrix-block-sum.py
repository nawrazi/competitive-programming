# https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                prefix[r][c] += mat[r][c]
                if c > 0:
                    prefix[r][c] += prefix[r][c - 1]
                if r > 0:
                    prefix[r][c] += prefix[r - 1][c]
                if c > 0 and r > 0:
                    prefix[r][c] -= prefix[r - 1][c - 1]
                    
        for r in range(rows):
            for c in range(cols):
                bottom, right = min(r + k, rows - 1), min(c + k, cols - 1)
                top, left = r - k - 1, c - k - 1
                
                block = prefix[bottom][right]
                if top >= 0 and right < cols:
                    block -= prefix[top][right]
                if bottom < rows and left >= 0:
                    block -= prefix[bottom][left]
                if top >= 0 and left >= 0:
                    block += prefix[top][left]
                    
                mat[r][c] = block
                
        return mat
    
