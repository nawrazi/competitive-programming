# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numset:
                length = 0
                counter = num
                while counter in numset:
                    counter += 1
                    length += 1
                longest = max(length, longest)

        return longest
