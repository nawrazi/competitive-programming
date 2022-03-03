# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        coins = 0
        for i in range(n//3, n, 2):
            coins += piles[i]

        return coins
