# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombinations(needed, base):
            if needed == 0:
                return [[]]
            
            combos = []
            for i in range(base, len(candidates)):
                if candidates[i] > needed:
                    continue
                for combo in getCombinations(needed - candidates[i], i):
                    combos.append(combo + [candidates[i]])
                    
            return combos
        
        return getCombinations(target, 0)
    
