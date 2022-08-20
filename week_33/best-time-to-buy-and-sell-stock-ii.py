# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_buy = last_sell = prices[0]
        total_profit = last_profit = 0
        
        for price in prices:
            if price < last_sell:
                last_buy = last_sell = price
                last_profit = 0
            elif price > last_sell:
                last_sell = price
                total_profit -= last_profit
                last_profit = last_sell - last_buy
                total_profit += last_profit
                
        return total_profit
    
