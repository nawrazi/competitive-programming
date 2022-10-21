# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def findLongest(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            if text1[idx1] == text2[idx2]:
                return 1 + findLongest(idx1 + 1, idx2 + 1)
            else:
                return max(findLongest(idx1, idx2 + 1), findLongest(idx1 + 1, idx2))
            
        return findLongest(0, 0)
    
