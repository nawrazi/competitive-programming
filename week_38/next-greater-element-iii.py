# https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(n) for n in str(n)]
        
        i, j = len(nums) - 2, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
            
        if i < 0:
            return -1
        
        while j < len(nums) and nums[j] > nums[i]:
            j += 1
        nums[i], nums[j-1] = nums[j-1], nums[i]
        
        j = len(nums) - 1
        i += 1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
        ans = int(''.join([str(n) for n in nums]))
        return ans if ans < 2 ** 31 else -1
    
