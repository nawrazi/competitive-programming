# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        
        for idx, num in enumerate(nums):
            left = bisect_left(nums, lower - num)
            right = bisect_right(nums, upper - num)
            count += right - left
            if left <= idx < right:
                count -= 1
                
        return count // 2
    
