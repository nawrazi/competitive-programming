# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1],[1,1]]

        for i in range(2, numRows):
            row = [1]
            for j in range(i - 1):
                row.append(triangle[i-1][j] + triangle[i-1][j+1])

            triangle.append(row + [1])

        return triangle if numRows > 1 else [triangle[0]]
