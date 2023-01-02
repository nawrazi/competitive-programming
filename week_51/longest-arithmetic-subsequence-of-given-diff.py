# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for num in reversed(arr):
            dp[num] = 1 + dp.get(num + difference, 0)
            
        return max(dp.values())
    
