# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_idx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx+=1
