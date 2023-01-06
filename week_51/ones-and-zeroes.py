# https://leetcode.com/problems/ones-and-zeroes/description/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def getSize(idx, counts):
            if idx >= len(strs):
                return 0
            
            zeros = strs[idx].count('0') + counts[0]
            ones = strs[idx].count('1') + counts[1]
            size = getSize(idx + 1, counts)
            
            if zeros <= m and ones <= n:
                size = max(size, 1 + getSize(idx + 1, (zeros, ones)))
                
            return size
        
        return getSize(0, (0, 0))
    
