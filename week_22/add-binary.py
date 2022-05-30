# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in list(a)]
        b = [int(i) for i in list(b)]
        rem = 0
        ans = []
        while a and b:
            if a[-1] != b[-1]:
                ans.append(str(1 - rem))
            else:
                ans.append(str(rem))
                rem = a[-1]
            a.pop()
            b.pop()
            
        long = a or b
        while long:
            if long[-1]:
                ans.append(str(1 - rem))
            else:
                ans.append(str(rem))
                rem = 0
            long.pop()
            
        if rem:
            ans.append('1')
        
        return ''.join(reversed(ans))
      