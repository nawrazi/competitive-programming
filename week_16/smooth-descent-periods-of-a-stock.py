# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[j - 1] - 1 == prices[j]:
                j += 1
            else:
                for k in range(j - i):
                    total += (j - i - k)
                i = j
                j += 1

        for k in range(j - i):
            total += (j - i - k)

        return total
