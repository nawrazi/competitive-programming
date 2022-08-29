# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getNext(self, nums):
        i, j = len(nums) - 2, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        
        while j < len(nums) and nums[j] > nums[i]:
            j += 1
        nums[i], nums[j-1] = nums[j-1], nums[i]
        
        j = len(nums) - 1
        i += 1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
        return nums
    
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        for _ in range(k - 1):
            nums = self.getNext(nums)
            
        return ''.join([str(n) for n in nums])
    
