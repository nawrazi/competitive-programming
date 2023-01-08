# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def getProfit(day, buying):
            if day >= len(prices):
                return 0
            
            if buying:
                pick = getProfit(day + 1, False) - prices[day]
                dont = getProfit(day + 1, True)
                
            else:
                pick = getProfit(day + 1, True) + prices[day] - fee
                dont = getProfit(day + 1, False)
                
            return max(pick, dont)
        
        return getProfit(0, True)
    
