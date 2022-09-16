# https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [[poured]]
        for i in range(query_row):
            cups.append([0 for _ in range(i + 2)])
            
        for i in range(1, len(cups)):
            for j in range(len(cups[i])):
                if j > 0:
                    cups[i][j] += max(0, (cups[i-1][j-1] - 1) / 2)
                if j < len(cups[i]) - 1:
                    cups[i][j] += max(0, (cups[i-1][j] - 1) / 2)
                    
        return min(1, cups[query_row][query_glass])
    
