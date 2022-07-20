# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            mid = (start + end) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                start = mid + 1
            elif g == -1:
                end = mid - 1
                
