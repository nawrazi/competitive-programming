# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def find(row, col):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]

            min_path = float(inf)
            for new_row, new_col in [(row, col + 1), (row + 1, col)]:
                if inBound(new_row, new_col):
                    if (new_row, new_col) in mem:
                        cur_path = mem[(new_row, new_col)]
                    else:
                        cur_path = find(new_row, new_col)
                        mem[(new_row, new_col)] = cur_path

                    min_path = min(min_path, grid[row][col] + cur_path)

            return min_path

        mem = {}
        inBound = lambda r,c : r < len(grid) and c < len(grid[0])

        return find(0, 0)
