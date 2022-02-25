# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1*num for num in nums]
        heapq.heapify(heap)
        
        for _ in range(k):
            top = heapq.heappop(heap)

        return top*-1
