# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def getCombinations(needed):
            if needed == 0:
                return 1
            
            combos = 0
            for i in range(len(nums)):
                if nums[i] > needed:
                    continue
                combos += getCombinations(needed - nums[i])
                    
            return combos
        
        return getCombinations(target)
    
