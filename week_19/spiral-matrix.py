# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def dfs(row, col, up):
            elements.append(matrix[row][col])
            seen.add((row, col))

            for x, y in directions if not up else reversed(directions):
                new_row, new_col = row + x, col + y
                if (new_row, new_col) not in seen and inBound(new_row, new_col):
                    dfs(new_row, new_col, (x,y) == (-1,0))

        directions = [(0,1), (1,0), (0,-1), (-1,0)] # R,D,L,U
        inBound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        seen = set()
        elements = []

        dfs(0,0,False)

        return elements
