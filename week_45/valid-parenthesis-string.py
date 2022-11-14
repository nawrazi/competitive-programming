# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def getValid(opened, idx):
            if idx >= len(s) or opened < 0:
                return opened == 0
            
            if s[idx] == '(':
                return getValid(opened + 1, idx + 1)
            
            if s[idx] == ')':
                return getValid(opened - 1, idx + 1)
            
            return getValid(opened + 1, idx + 1) or getValid(opened - 1, idx + 1) or getValid(opened, idx + 1)
        
        return getValid(0, 0)
    
