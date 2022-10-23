# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        left, right = 0, 1
        used = False
        cur_max = -inf
        while right < len(nums):
            if nums[right] < nums[left]:
                if used:
                    return False
                elif nums[right] >= cur_max:
                    nums[left] = nums[right]
                else:
                    nums[right] = nums[left]
                used = True
                
            cur_max = nums[left]
            left += 1
            right += 1
            
        return True
    
