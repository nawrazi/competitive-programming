# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicates.append(abs(num))
            nums[idx] *= -1
            
        return duplicates
    
