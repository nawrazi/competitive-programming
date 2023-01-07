# https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a.find(b) != -1:
            return 1
        
        start = b.find(a)
        if start == -1:
            return 2 if (a + a).find(b) != -1 else -1
        
        if start != 0 and a[-start:] != b[:start]:
            return -1
        
        reps = 2 - int(start == 0)
        idx1, idx2 = start + len(a), 0
        
        while idx1 < len(b):
            if b[idx1] != a[idx2 % len(a)]:
                return -1
            if idx2 % len(a) == 0:
                reps += 1
            idx1 += 1
            idx2 += 1
            
        return reps
    
