# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        seen = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # R,D,L,U
        inBound = lambda r, c, rim: rim <= r < len(matrix) - rim and rim <= c < len(matrix[0]) - rim
        rimSize = {}
        
        def dfs(rim, row, col, up):
            cur = matrix[row][col]
            
            if len(queue) == rimSize[i] and (row, col) not in replaced:
                matrix[row][col] = queue.popleft()
                replaced.add((row, col))
            elif replaced:
                return
            
            queue.append(cur)
            
            if row != rim:
                seen.add((row, col))
                
            for x, y in directions if not up else reversed(directions):
                new_row, new_col = row + x, col + y
                if (new_row, new_col) not in seen and inBound(new_row, new_col, rim):
                    dfs(rim, new_row, new_col, (x,y) == (-1,0))
                    return
                
        for i in range(len(matrix) // 2):
            replaced = set()
            queue = deque()
            rimSize[i] = len(matrix) - (i * 2) - 1
            dfs(i, i, i, False)
            
