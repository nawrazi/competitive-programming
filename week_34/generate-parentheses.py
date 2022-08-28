# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def getAll(opened, length):
            if length == (2 * n) - 1:
                return [[')']]
            
            nex = []
            if opened > 0:
                nex_close = getAll(opened - 1, length + 1)
                for combo in nex_close:
                    combo.insert(0, ')')
                    
                nex += nex_close
                
            if opened < (2 * n) - length:
                nex_open = getAll(opened + 1, length + 1)
                for combo in nex_open:
                    combo.insert(0, '(')
                    
                nex += nex_open
            
            return nex
        
        return [''.join(combo) for combo in getAll(0, 0)]
    
