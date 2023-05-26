# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def check(idx1, idx2):
            if idx1 == len(s):
                return True
            
            if idx2 == len(t):
                return False
            
            if s[idx1] == t[idx2]:
                return check(idx1 + 1, idx2 + 1)
            
            return check(idx1, idx2 + 1)
        
        return check(0, 0)
    
