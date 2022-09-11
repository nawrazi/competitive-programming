# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        cur = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == cur:
                count += 1
            else:
                cur = nums[i]
                count = 1
            if count > 2:
                dup.append(i)
                count += 1
            
        slots = len(nums) - len(dup)
        while dup:
            idx = dup.pop()
            while idx < len(nums) - 1:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                idx += 1
                
        return slots
    
