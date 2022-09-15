# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        mid = 0
        
        while start < end:
            mid = (start + end) // 2
            if start == end - 1 and nums[start] > nums[end]:
                return nums[end]
            
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
                return nums[0]
            
        return nums[mid]
    
