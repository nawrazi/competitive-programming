# https://leetcode.com/problems/find-in-mountain-array/

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        
        left, right = 0, size - 1
        while left <= right:
            mid = (left + right) // 2
            
            if mid > 0 and mountain_arr.get(mid) < mountain_arr.get(mid - 1):
                right = mid - 1
            elif mid < size - 1 and mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                peak = mid
                break
                
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            
            if target > mountain_arr.get(mid):
                left = mid + 1
            elif target < mountain_arr.get(mid):
                right = mid - 1
            else:
                return mid
            
        left, right = peak, size - 1
        while left <= right:
            mid = (left + right) // 2
            
            if target > mountain_arr.get(mid):
                right = mid - 1
            elif target < mountain_arr.get(mid):
                left = mid + 1
            else:
                return mid
            
        return -1
    
