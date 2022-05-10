# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        final = []
        
        i, j = 0, 1
        while j < len(nums) + 1:
            if j == len(nums) or nums[j] - nums[j-1] != 1:
                final.append(f"{nums[i]}->{nums[j-1]}" if i != j - 1 else f"{nums[i]}")
                i = j
            j += 1
            
        return final
