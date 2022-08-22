# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        
        def getCombinations(needed, base, length):
            if needed == 0 and length == k:
                return [[]]
            
            combos = []
            for i in range(base, len(candidates)):
                if candidates[i] > needed:
                    break
                for combo in getCombinations(needed - candidates[i], i + 1, length + 1):
                    combos.append(combo + [candidates[i]])
                    
            return combos
        
        return getCombinations(n, 0, 0)
    
