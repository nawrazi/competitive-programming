# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def loot(pos, got_1):
            if pos >= len(nums):
                return 0
            
            if got_1 and pos == len(nums) - 1 and len(nums) > 1:
                return 0
            
            if pos + 2 not in cache:
                cache[pos + 2] = loot(pos + 2, got_1)
                
            if pos + 3 not in cache:
                cache[pos + 3] = loot(pos + 3, got_1)
            
            return nums[pos] + max(cache[pos + 2], cache[pos + 3])
        
        cache = {}
        a = loot(0, True)
        cache.clear()
        b = loot(1, False)
        c = loot(2, False)
        
        return max(a, b, c)
    
