# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def count(idx1, idx2):
            if idx1 >= len(s1) or idx2 >= len(s2):
                return sum(ord(c) for c in s2[idx2:]) + sum(ord(c) for c in s1[idx1:])
            
            if s1[idx1] == s2[idx2]:
                return count(idx1 + 1, idx2 + 1)
            
            return min(ord(s1[idx1]) + count(idx1 + 1, idx2), ord(s2[idx2]) + count(idx1, idx2 + 1))
        
        return count(0, 0)
    
