# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        max_ones = 0
        
        while j < len(nums):
            while j < len(nums) and (nums[j] == 1 or k > 0):
                k -= 1 - nums[j]
                j += 1
            max_ones = max(max_ones, j - i)
            while i < j and nums[i] == 1:
                i += 1
            if i != j:
                k += 1
            i += 1
            j = max(j, i)
            
        return max_ones
    
