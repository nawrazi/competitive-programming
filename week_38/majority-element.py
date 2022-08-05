# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        mask = 1
        for _ in range(31):
            maj = 0
            for num in nums:
                if num & mask:
                    maj += 1
                else:
                    maj -= 1
                    
            if maj > 0:
                ans |= mask
                
            mask <<= 1
                
        return ans
    
