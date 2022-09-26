# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s: str) -> bool:
        nume, numE = s.split('e'), s.split('E')
        n = max(nume, numE, key = lambda x: len(x))
        s = len(nume) + len(numE)
        
        if len(n) > 2 or s > 3:
            return False
        
        for i, p in enumerate(n):
            numP, numM = p.split('+'), p.split('-')
            m = max(numP, numM, key = lambda x: len(x))
            s = len(numP) + len(numM)
            
            if len(m) > 1 and not m[0] and not m[1]:
                return False
            
            if not p or len(m) > 2 or s > 3 or (len(m) == 2 and len(m[0]) > 0):
                return False
            
            if i == 1 and (len(p.split('.')) > 1 or not m[-1].isnumeric()):
                return False
        
        dec = max(n[0].split('+'), n[0].split('-'), key = lambda x: len(x))[-1].split('.')
        
        if len(dec) == 1 and dec[0].isnumeric():
            return True
        
        if len(dec) != 2 or (not dec[0] and not dec[1]):
            return False
        
        return len(dec) == 2 and (dec[0].isnumeric() or not dec[0]) and (dec[1].isnumeric() or not dec[1])
    
