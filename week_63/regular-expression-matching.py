# https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def match(si, pi):
            if si >= len(s) and pi >= len(p):
                return True
            if si >= len(s) or pi >= len(p):
                if pi + 1 < len(p) and p[pi + 1] == '*':
                    return match(si, pi + 2)
                return False
            
            if pi == len(p) - 1 or p[pi + 1] != '*':
                return p[pi] in {s[si], '.'} and match(si + 1, pi + 1)
            
            sn = si
            while sn < len(s) and p[pi] in {s[sn], '.'}:
                if match(sn + 1, pi + 2):
                    return True
                sn += 1
                
            return match(si, pi + 2)
        
        return match(0, 0)
    
