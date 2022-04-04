# https://leetcode.com/contest/weekly-contest-227/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        drop = 0
        dropped = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if dropped:
                    return False
                drop = nums[i-1]
                dropped = True

        return not dropped or nums[0] >= nums[-1]
