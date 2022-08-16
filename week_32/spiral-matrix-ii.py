# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        def dfs(row, col, up, val):
            matrix[row][col] = val
            seen.add((row, col))
            
            for x, y in directions if not up else reversed(directions):
                new_row, new_col = row + x, col + y
                if (new_row, new_col) not in seen and inBound(new_row, new_col):
                    dfs(new_row, new_col, (x,y) == (-1,0), val + 1)
                    
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # R,D,L,U
        inBound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        seen = set()
        
        dfs(0, 0, False, 1)
        
        return matrix
    
