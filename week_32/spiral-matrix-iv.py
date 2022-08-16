# https://leetcode.com/problems/spiral-matrix-iv/

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        def dfs(row, col, up, node):
            if not node:
                return
            matrix[row][col] = node.val
            seen.add((row, col))
            
            for x, y in directions if not up else reversed(directions):
                new_row, new_col = row + x, col + y
                if (new_row, new_col) not in seen and inBound(new_row, new_col):
                    dfs(new_row, new_col, (x,y) == (-1,0), node.next)
                    return
                    
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # R,D,L,U
        inBound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        seen = set()
        
        dfs(0, 0, False, head)
        
        return matrix
    
