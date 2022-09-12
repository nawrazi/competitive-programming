# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [n for n, c in Counter(nums).items() if c > len(nums) / 3]
