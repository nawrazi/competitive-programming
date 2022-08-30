# https://leetcode.com/problems/magical-string/

class Solution:
    def magicalString(self, n: int) -> int:
        opp = {'1': '2', '2': '1'}
        s = '122'
        cur = '2'
        size = 3
        i = 2
        
        while size < n:
            s += opp[cur] * int(s[i])
            cur = opp[cur]
            size += int(s[i])
            i += 1
            
        return Counter(s[:n])['1']
    
