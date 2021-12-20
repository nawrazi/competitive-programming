# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        n = len(piles)
        coins = 0
        for i in range(n//3, len(piles), 2):
            coins += piles[i]
            print(i)

        return coins
