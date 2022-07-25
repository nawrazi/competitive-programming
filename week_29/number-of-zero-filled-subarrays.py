# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(1)
        slow, fast = 0, 0
        counting = False
        ans = 0
        
        while fast < len(nums):
            if nums[fast] == 0:
                if not counting:
                    slow = fast
                    counting = True
            elif counting:
                n = fast - slow
                ans += n * (n + 1) // 2
                counting = False
            fast += 1
            
        return ans
    
