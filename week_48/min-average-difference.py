# https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        min_average = [inf, 0]
        for idx, num in enumerate(nums, 1):
            left_ave = prefix[idx] // idx
            right_ave = (prefix[-1] - prefix[idx]) // (len(nums) - idx) if idx < len(nums) else 0
            min_average = min(min_average, [abs(left_ave - right_ave), idx - 1])
            
        return min_average[1]
    
