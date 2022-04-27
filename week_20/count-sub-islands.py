# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def isSub(row,col):
            grid2[row][col] = 2
            flag = True
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if inBound(new_row, new_col) and grid2[new_row][new_col] == 1:
                    flag = isSub(new_row, new_col) and flag

            return grid1[row][col] == 1 and flag

        sub_islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inBound = lambda r, c : 0 <= r < len(grid2) and 0 <= c < len(grid2[0])

        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and isSub(row, col):
                    sub_islands += 1

        return sub_islands
