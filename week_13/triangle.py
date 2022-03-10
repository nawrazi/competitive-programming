# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def findSum(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]

            min_sum = float(inf)
            for new_col in [col, col+1]:
                if new_col < len(triangle[row+1]):
                    if (row, new_col) in mem:
                        nex = mem[(row, new_col)]
                    else:
                        nex = findSum(row+1,new_col)
                        mem[(row, new_col)] = nex

                    min_sum = min(min_sum, triangle[row][col] + nex)

            return min_sum

        mem = {}
        return findSum(0,0)
