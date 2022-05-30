# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        
        return [heappop(nums) for _ in range(len(nums))]
      
