# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1],[1,1]]

        for i in range(2, rowIndex + 1):
            row = [1]
            for j in range(i - 1):
                row.append(triangle[i-1][j] + triangle[i-1][j+1])

            triangle.append(row + [1])

        return triangle[rowIndex]
