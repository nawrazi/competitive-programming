# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @cache
        def getSum(cur, sign):
            if cur >= len(nums):
                return 0
            
            pick = (sign * nums[cur]) + getSum(cur + 1, -sign)
            dont = getSum(cur + 1, sign)
            
            return max(pick, dont)
        
        return getSum(0, 1)
    
