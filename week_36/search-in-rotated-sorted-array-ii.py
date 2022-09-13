# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        pivot = n
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                pivot = i
                break
                
        if target >= nums[0]:
            start, end = 0, pivot - 1
        else:
            start, end = pivot, n - 1
            
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return True
            
        return False
    
