# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0 for _ in range(101)]
        total = 0

        for i in range(n):
            freq[nums[i]]+=1

        for i in range(101):
            total += int(freq[i] * (freq[i]-1) * 0.5)

        return total
