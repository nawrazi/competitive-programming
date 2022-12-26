# https://leetcode.com/problems/largest-divisible-subset/description/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def getLongest(idx, last):
            if idx >= len(nums):
                return ()
            
            dont = getLongest(idx + 1, last)
            pick = ()
            if nums[idx] % last == 0:
                pick = getLongest(idx + 1, nums[idx]) + (nums[idx],)
                
            return max(pick, dont, key=len)
        
        nums.sort()
        return getLongest(0, 1)
    
