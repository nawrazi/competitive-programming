# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        
        nums.sort()
        min_range = inf
        i, j = 0, len(nums) - 4
        
        while j < len(nums):
            min_range = min(min_range, nums[j] - nums[i])
            i += 1
            j += 1
            
        return min_range
    
