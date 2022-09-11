# https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ''
        
        while a or b:
            if a > b:
                if len(s) < 2 or s[-1] + s[-2] != 'aa':
                    s += 'a'
                    a -= 1
                else:
                    s += 'b'
                    b -= 1
                    
            else:
                if len(s) < 2 or s[-1] + s[-2] != 'bb':
                    s += 'b'
                    b -= 1
                else:
                    s += 'a'
                    a -= 1
                    
        return s
    
