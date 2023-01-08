# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def getProfit(day, buying, trans):
            if day >= len(prices):
                return 0
            
            if buying:
                pick = getProfit(day + 1, False, trans) - prices[day]
                dont = getProfit(day + 1, True, trans)
                
            else:
                pick = prices[day]
                if trans < k - 1:
                    pick += getProfit(day + 1, True, trans + 1)
                dont = getProfit(day + 1, False, trans)
                
            return max(pick, dont)
        
        return getProfit(0, True, 0)
    
