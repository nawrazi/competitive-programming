# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def search(self, nums, target, isLeft):
        left, right = 0, len(nums)-1
        best = -1

        while left<=right:
            mid = (left+right)//2

            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                best = mid
                if isLeft:
                    right = mid-1
                else:
                    left = mid+1

        return best

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target, True), self.search(nums, target, False)]
