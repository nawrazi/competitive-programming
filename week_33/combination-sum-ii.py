# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombinations(needed, base):
            if needed == 0:
                return [[]]
            
            combos = []
            for i in range(base, len(candidates)):
                if candidates[i] > needed:
                    break
                if i != base and candidates[i] == candidates[i - 1]:
                    continue
                for combo in getCombinations(needed - candidates[i], i + 1):
                    combos.append(combo + [candidates[i]])
                    
            return combos
        
        candidates.sort()
        return getCombinations(target, 0)
    
