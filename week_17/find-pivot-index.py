# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum, left_sum = sum(nums), 0

        for i, num in enumerate(nums):
            right_sum -= num
            
            if right_sum == left_sum:
                return i

            left_sum += num

        return -1
