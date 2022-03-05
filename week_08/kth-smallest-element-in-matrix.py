# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for i in range(len(matrix)):
            heapq.heappush(heap,(matrix[i][0],i,0))

        for _ in range(k):
            val, row, idx = heapq.heappop(heap)
            if idx+1<len(matrix) and row<len(matrix):
                heapq.heappush(heap,(matrix[row][idx+1],row,idx+1))

        return val
