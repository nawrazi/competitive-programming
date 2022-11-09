# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                
        return [duplicate, missing]
    
