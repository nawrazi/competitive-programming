# https://leetcode.com/problems/minimize-maximum-of-array/description/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = sum(nums)
        
        for idx in range(len(nums) - 1, 0, -1):
            ideal = ceil(total / (idx + 1))
            if nums[idx] > ideal:
                diff = nums[idx] - ideal
                nums[idx] -= diff
                nums[idx - 1] += diff
            total -= nums[idx]
        
        return max(nums)
    
