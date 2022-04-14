# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        stop = 0
        for i in range(1, n + 1):
            stop = (stop + k) % i

        return stop + 1
