# https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        @cache
        def search(idx):
            seen.add(idx)
            size = 1
            if nums[idx] not in seen:
                size += search(nums[idx])
            seen.remove(idx)
            return size
        
        max_size = 0
        for i in range(len(nums)):
            seen = set()
            max_size = max(max_size, search(i))
        
        return max_size
    
