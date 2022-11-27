# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        numbers = 0
        for i in range(1, len(s)):
            numbers += pow(len(digits), i)
        
        def getNums(idx):
            if idx >= len(s):
                return 1
            
            full = bisect_left(digits, s[idx])
            cur = full * pow(len(digits), len(s) - idx - 1)
            
            if full == len(digits) or s[idx] < digits[full]:
                return cur
            
            return cur + getNums(idx + 1)
        
        return numbers + getNums(0)
    
