# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        ones1, ones2 = s.count('1'), target.count('1')
        
        if (ones1 > 0 and ones2 > 0) or (ones1 == ones2 == 0):
            return True
        
