# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        
        for i, num in enumerate(nums):
            if num in last and abs(last[num] - i) <= k:
                return True
            last[num] = i
        
        return False
    
