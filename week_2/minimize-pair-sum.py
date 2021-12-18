# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/submissions/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0

        while nums:
            max_sum = max(nums.pop(0) + nums.pop(), max_sum)

        return max_sum
