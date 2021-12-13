# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/submissions/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        for i in range(0,n-1,2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums
