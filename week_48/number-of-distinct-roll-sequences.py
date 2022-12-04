# https://leetcode.com/problems/number-of-distinct-roll-sequences/

class Solution:
    def distinctSequences(self, n: int) -> int:
        common = {2: {4, 6}, 3: {6}, 4: {2, 6}, 6: {2, 3, 4}}
        mod = pow(10, 9) + 7
        
        @cache
        def getSequences(rolls, last):
            if rolls == n:
                return 1
            
            sequences = 0
            for nex in range(1, 7):
                if nex not in last and nex not in common.get(last[1], set()):
                    sequences = (sequences + getSequences(rolls + 1, (last[1], nex))) % mod
                    
            return sequences % mod
        
        return getSequences(0, (0, 0))
    
