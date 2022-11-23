# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digits = list(str(n))
        total = sum(int(n) for n in digits)
        addition = 0
        power = 1
        
        while digits and total > target:
            last = int(digits.pop())
            total -= last
            if power == 1:
                addition += 10 - last
                total += 1
            else:
                addition += power * (10 - last - 1)
            power *= 10
            
        return addition
    
