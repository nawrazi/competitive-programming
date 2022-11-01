# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def check(si, pi):
            if si >= len(s) and pi >= len(p):
                return True
            if si >= len(s) and p[pi] == '*':
                return check(si, pi + 1)
            if si >= len(s) or pi >= len(p):
                return False
            if p[pi] not in ['*', '?', s[si]]:
                return False
            
            if p[pi] in ['?', s[si]]:
                return check(si + 1, pi + 1)
            
            # compress successive stars
            while pi < len(p) - 1 and p[pi + 1] == '*':
                pi += 1
                
            if pi == len(p) - 1:
                return True

            while si < len(s):
                if p[pi + 1] in ['?', s[si]] and check(si, pi + 1):
                    return True
                si += 1
                    
        return check(0, 0)
    
