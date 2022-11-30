# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx1, idx2 = 0, 0
        while idx1 < len(s) and idx2 < len(t):
            if s[idx1] == t[idx2]:
                idx2 += 1
            idx1 += 1
            
        return len(t) - idx2
    
