# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying = 0

        for selling in range(len(prices)):
            if prices[selling] < prices[buying]:
                buying = selling
            max_profit = max(max_profit, prices[selling] - prices[buying])

        return max_profit
