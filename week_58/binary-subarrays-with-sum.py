# https://leetcode.com/problems/binary-subarrays-with-sum/description/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = Counter()
        count = 0
        
        for num in accumulate(nums, initial=0):
            count += seen[num - goal]
            seen[num] += 1
            
        return count
    
