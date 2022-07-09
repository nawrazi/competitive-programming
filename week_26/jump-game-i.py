class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums) - 1
        i = j - 1
        
        while i >= 0:
            if i + nums[i] >= j:
                j = i
            i -= 1
            
        return j == 0
    
