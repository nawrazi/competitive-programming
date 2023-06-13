# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        if set(s) == {'a'}:
            return ''.join(s[:-1] + ['z'])
        
        idx1 = 0
        while idx1 < len(s) and s[idx1] == 'a':
            idx1 += 1
            
        idx2 = idx1
        while idx2 < len(s) and s[idx2] != 'a':
            s[idx2] = chr(ord(s[idx2]) - 1)
            idx2 += 1
            
        return ''.join(s)
    
