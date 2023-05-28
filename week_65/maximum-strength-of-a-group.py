# https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        self.max = max(nums)
        
        def search(idx, strength, picked):
            if idx == len(nums):
                if picked:
                    self.max = max(self.max, strength)
                return
            
            search(idx + 1, nums[idx] * strength, True)
            search(idx + 1, strength, picked)
            
        search(0, 1, False)
        return self.max
    
