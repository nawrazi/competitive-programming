# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def findWay(cur, target):
            if target == 0:
                return True
            if cur >= len(nums) or target < 0:
                return False
            
            return findWay(cur + 1, target - nums[cur]) or findWay(cur + 1, target)
        
        if sum(nums) % 2 == 1:
            return False
        
        return findWay(0, sum(nums) / 2)
    
