# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/description/

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        score = int(nums[0] > 0)
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            score += int(nums[i] > 0)
            
        return score
    
