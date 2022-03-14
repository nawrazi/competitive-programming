# https://leetcode.com/problems/smallest-range-ii/submissions/

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_score = nums[~0] - nums[0]

        for i in range(len(nums) - 1):
            cur_max = max(nums[~0] - k, nums[i] + k)
            cur_min = min(nums[0] + k, nums[i+1] - k)
            cur_score = cur_max - cur_min
            min_score = min(min_score, cur_score)

        return min_score
