# https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def value(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + value(num // 2)
            else:
                return 1 + value((3 * num) + 1)
            
        values = list(range(lo, hi + 1))
        values.sort(key = value)
        return values[k - 1]
    
