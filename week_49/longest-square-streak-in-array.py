# https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squares = set(nums)
        max_streak = -1
        
        for num in nums:
            cur = num
            streak = 1
            while pow(cur, 2) in squares:
                cur = pow(cur, 2)
                streak += 1
                max_streak = max(streak, max_streak)
                
        return max_streak
    
