# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        count = 1
        limit = len(nums)
        
        i = 1
        while i < limit:
            if nums[i] == cur:
                count += 1
            else:
                cur = nums[i]
                count = 1
            if count > 2:
                limit -= 1
                count -= 1
                idx = i
                while idx < limit:
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                    idx += 1
                continue
                
            i += 1
            
        return limit
    
