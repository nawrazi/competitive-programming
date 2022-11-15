# https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        slices = 0
        for i in range(len(nums) - 2):
            diff = None
            for j in range(i + 1, len(nums)):
                if diff is None:
                    diff = nums[j] - nums[i]
                elif nums[j] - nums[j - 1] == diff:
                    slices += 1
                else:
                    break
                    
        return slices
    
