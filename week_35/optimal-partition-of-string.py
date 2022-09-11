# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        sets = 1
        
        for c in s:
            if c in cur:
                cur = {c}
                sets += 1
            else:
                cur.add(c)
                
        return sets
    
