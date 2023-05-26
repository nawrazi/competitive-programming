# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        inc = []
        dp = []
        peak = -1
        for idx, num in enumerate(nums):
            pos = bisect_left(dp, num)
            
            if pos == len(dp):
                dp.append(num)
                peak = idx
            else:
                dp[pos] = num
                
            inc.append((len(dp), peak))
            
        dp = []
        longest = 0
        for idx, num in enumerate(reversed(nums)):
            pos = bisect_left(dp, num)
            
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
                
            if inc[~idx][0] == 1 or len(dp) == 1:
                continue
            
            mountain = inc[~idx][0] + len(dp) - int(nums[inc[~idx][1]] == num)
            longest = max(longest, mountain)
            
        return len(nums) - longest
    
