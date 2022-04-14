# https://leetcode.com/problems/predict-the-winner/

class Solution:
    def PredictTheWinner(self, nums):
        @lru_cache(None)
        def findWinner(left, right, turn):
            if left == right:
                return turn * nums[left]

            choose_left = turn * nums[left] + findWinner(left + 1, right, -turn)
            choose_right = turn * nums[right] + findWinner(left, right - 1, -turn)

            return turn * max(turn * choose_left, turn * choose_right)

        return findWinner(0, len(nums) - 1, 1) >= 0
        
