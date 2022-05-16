# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mask = 0
        for i, num in enumerate(nums):
            mask ^= num
            mask ^= i
            
        return mask ^ len(nums)
    
