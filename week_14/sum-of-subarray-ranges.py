# https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        i, j = 0, 1
        total = 0

        while i < len(nums) - 1:
            cur_max, cur_min = float(-inf), float(inf)

            while j < len(nums):
                cur_max = max(cur_max, nums[i], nums[j])
                cur_min = min(cur_min, nums[i], nums[j])

                total += cur_max - cur_min
                j += 1

            i += 1
            j = i + 1

        return total
