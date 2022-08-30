# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = defaultdict(lambda: '')
        fac = (2 * numRows) - 2
        peak = numRows - 1
        
        for i, c in enumerate(s):
            rows[abs(peak - (i % fac))] += c
            
        ans = ''
        for i in range(numRows, -1, -1):
            ans += rows[i]
            
        return ans
    
