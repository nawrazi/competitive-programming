# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def getProfit(day, buying, cooling):
            if day >= len(prices):
                return 0
            
            if buying:
                dont = getProfit(day + 1, True, False)
                if cooling:
                    return dont
                else:
                    return max(dont, getProfit(day + 1, False, False) - prices[day])
                
            else:
                pick = getProfit(day + 1, True, True) + prices[day]
                dont = getProfit(day + 1, False, False)
                return max(pick, dont)
            
        return getProfit(0, True, False)
    
