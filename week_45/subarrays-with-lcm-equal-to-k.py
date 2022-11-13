# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        total = 0
        
        for i, num in enumerate(nums):
            if num == k:
                total += 1
            mult = num
            for j in range(i + 1, len(nums)):
                mult = lcm(mult, nums[j])
                if mult == k:
                    total += 1
                    
        return total
    
