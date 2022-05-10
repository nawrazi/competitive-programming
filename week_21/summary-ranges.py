# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        final = []
        
        i, j = 0, 1
        while j < len(nums):
            diff = nums[j] - nums[j-1]
            if diff != 1:
                output = f"{nums[i]}->{nums[j-1]}" if i != j - 1 else f"{nums[i]}"
                final.append(output)
                i = j
            j += 1
            
        if nums:
            final.append(f"{nums[i]}->{nums[j-1]}" if i != j - 1 else f"{nums[i]}")
        
        return final
