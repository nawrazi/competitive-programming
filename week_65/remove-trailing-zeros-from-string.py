# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l = list(num)
        while l and l[-1] == '0':
            l.pop()
            
        return ''.join(l)
    
