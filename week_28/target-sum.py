# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def getWays(idx, cur):
            if idx == len(nums):
                return int(cur == target)
            
            if (idx, cur) not in cache:
                cache[(idx, cur)] = getWays(idx+1, cur+nums[idx]) + getWays(idx+1, cur-nums[idx])
                
            return cache[(idx, cur)]
            
        cache = {}
        return getWays(0, 0)
    
