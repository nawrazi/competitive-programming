# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/description/

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        slope = lambda x1, y1, x2, y2: (y2 - y1, x2 - x1)
        bend = lambda y1, x1, y2, x2: y2 * x1 != y1 * x2
        cur_slope = None
        lines = 0
        
        for i in range(1, len(stockPrices)):
            new_slope = slope(*stockPrices[i], *stockPrices[i - 1])
            if cur_slope is None or bend(*cur_slope, *new_slope):
                cur_slope = new_slope
                lines += 1
                
        return lines
    
