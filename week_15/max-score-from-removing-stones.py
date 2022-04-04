# https://leetcode.com/contest/weekly-contest-227/problems/maximum-score-from-removing-stones/

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = sorted([a,b,c])
        score = 0

        while piles[0] + piles[1] > 0:
            while piles[0] > 0 and piles[2] > piles[1]:
                piles[0] -= 1
                piles[2] -= 1
                score += 1
            while piles[0] > 0 and piles[2] <= piles[1]:
                piles[1] -= 1
                piles[0] -= 1
                score += 1
            while piles[0] == 0 and piles[1] >= 1:
                piles[1] -= 1
                piles[2] -= 1
                score += 1

        return score
