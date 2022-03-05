# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix[0])
        start, end = 0, (len(matrix)*row_length)-1

        while start<=end:
            mid = (start+end)//2
            val = matrix[mid//row_length][mid%row_length]

            if val>target:
                end = mid-1
            elif val<target:
                start = mid+1
            else:
                return True

        return False
