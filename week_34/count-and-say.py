# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        
        for _ in range(n - 1):
            new = ''
            cur, count = ans[0], 0
            for c in ans:
                if c != cur:
                    new += f'{count}{cur}'
                    cur, count = c, 1
                else:
                    count += 1
            
            ans = new + f'{count}{cur}'
            
        return ans
    
