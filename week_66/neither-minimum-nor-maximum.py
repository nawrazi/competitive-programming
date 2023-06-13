# https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)
        for num in nums:
            if num != mx and num != mn:
                return num
            
        return -1
    
