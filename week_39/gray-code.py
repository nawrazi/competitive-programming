# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        used = {0}
        code = [0]
        
        def getCode():
            if len(code) == 2 ** n:
                diff = 0
                for i in range(n):
                    if (code[-1] & 1 << i) ^ (0 & 1 << i):
                        diff += 1
                    
                return diff == 1
            
            for s in range(n):
                nex = 0
                for i in range(n):
                    bit = 1 if code[-1] & 1 << i else 0
                    nex |= (1 - bit) << i if i == s else bit << i
                    
                if nex not in used:
                    code.append(nex)
                    used.add(nex)
                    if getCode():
                        return True
                    used.remove(nex)
                    code.pop()
                    
        getCode()
        return code
    
