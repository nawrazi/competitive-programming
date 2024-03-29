# https://leetcode.com/problems/magical-string/

class Solution:
    def magicalString(self, n: int) -> int:
        opp = {'1': '2', '2': '1'}
        s = '122'
        cur = '1'
        size = 3
        i = 2
        
        while size < n:
            s += cur * int(s[i])
            cur = opp[cur]
            size += int(s[i])
            i += 1
            
        return s[:n].count('1')
    
