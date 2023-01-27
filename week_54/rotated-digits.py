# https://leetcode.com/problems/rotated-digits/description/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        self.good = 0
        digits = {0, 1, 2, 5, 6, 8, 9}
        asymmetric = {2, 5, 6, 9}
        cur = []
        
        def backtrack(valid, first):
            if cur and int(''.join(cur)) > n:
                return
            
            self.good += valid
            
            for digit in digits:
                if not (first and digit == 0):
                    cur.append(str(digit))
                    backtrack(valid or digit in asymmetric, False)
                    cur.pop()
        
        backtrack(False, True)
        return self.good
    
