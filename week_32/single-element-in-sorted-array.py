# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid % 2 == 0 and mid < len(nums) - 1:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
            elif mid > 0:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
            else:
                break
                
        if mid % 2 == 1 and nums[mid] == nums[mid - 1]:
            return nums[mid + 1]
        else:
            return nums[mid]
        
