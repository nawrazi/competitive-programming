# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if mid > 0 and arr[mid] < arr[mid - 1]:
                end = mid - 1
            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                return mid
            
