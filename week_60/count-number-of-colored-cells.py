# https://leetcode.com/problems/count-total-number-of-colored-cells/description/

class Solution:
    def coloredCells(self, n: int) -> int:
        cardinal = 4 * (n - 1)
        fillers = 2 * (n - 2) * (n - 1)
        return 1 + cardinal + fillers
    
