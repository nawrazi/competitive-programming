# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def search(self,row):
        start, end = 0, len(row)-1
        best = len(row)

        while start<=end:
            middle = (start+end)//2

            if row[middle]<0:
                best = middle
                end = middle-1
            else:
                start = middle+1

        return len(row)-best

    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for row in grid:
            total += self.search(row)

        return total
