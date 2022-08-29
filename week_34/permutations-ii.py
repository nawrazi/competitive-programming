# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        ans = set()
        
        def getPerms(cur):
            if len(cur) == len(nums):
                ans.add(tuple(cur))
                return
            
            for i, num in enumerate(nums):
                if i not in seen:
                    seen.add(i)
                    getPerms(cur + [num])
                    seen.remove(i)
                
        getPerms([])
        return ans
    
