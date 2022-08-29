# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i, j = len(nums) - 2, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        
        if i < 0:
            nums.sort()
            return
        
        while j < len(nums) and nums[j] > nums[i]:
            j += 1
        nums[i], nums[j-1] = nums[j-1], nums[i]
        
        j = len(nums) - 1
        i += 1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
