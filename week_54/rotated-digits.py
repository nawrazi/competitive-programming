# https://leetcode.com/problems/rotated-digits/description/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = {0, 1, 2, 5, 6, 8, 9}
        asymmetric = {2, 5, 6, 9}
        cur = 0
        good = 0
        
        def backtrack(valid, first):
            nonlocal cur, good
            if cur > n:
                return
            
            good += valid
            
            for digit in digits:
                if not (first and digit == 0):
                    cur = (cur * 10) + digit
                    backtrack(valid or digit in asymmetric, False)
                    cur //= 10
        
        backtrack(False, True)
        return good
    
