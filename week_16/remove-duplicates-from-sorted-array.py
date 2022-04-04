# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        swap = 0
        for i in range(len(nums)):
            if nums[i] != nums[swap]:
                swap += 1
                nums[swap], nums[i] = nums[i], nums[swap]

        return swap + 1
