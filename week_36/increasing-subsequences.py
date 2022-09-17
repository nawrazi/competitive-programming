# https://leetcode.com/problems/increasing-subsequences/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nums.append(inf)
        total = set()
        sub = []
        def getSubs(cur):
            if cur >= len(nums):
                return
            
            if len(sub) > 1:
                total.add(tuple(sub))
                
            for i in range(cur + 1, len(nums)):
                if nums[i] >= nums[cur]:
                    sub.append(nums[cur])
                    getSubs(i)
                    sub.pop()
                    
        for i in range(len(nums) - 1):
            getSubs(i)
            
        return total
    
