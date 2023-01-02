# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for i in range(len(arr) - 1, -1, -1):
            dp[arr[i]] = 1 + dp.get(arr[i] + difference, 0)
            
        return max(dp.values())
    
