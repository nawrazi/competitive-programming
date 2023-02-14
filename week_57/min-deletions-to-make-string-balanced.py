# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        aAfter, bBefore = [0], [0]
        for i in range(len(s)):
            aAfter.append(aAfter[-1] + int(s[~i] == 'a'))
            bBefore.append(bBefore[-1] + int(s[i] == 'b'))
            
        min_del = inf
        for a, b in zip(reversed(aAfter), bBefore):
            min_del = min(min_del, a + b)
            
        return min_del
    
