# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        low, high = 0, 0
        for num in nums:
            prefix += num
            low = min(low, prefix)
            high = max(high, prefix)
            
        return abs(low) + abs(high)
    
