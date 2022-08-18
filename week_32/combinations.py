# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def search(base, size):
            if size == k:
                return [[]]
            
            combs = []
            for i in range(base + 1, n + 1):
                nex = search(i, size + 1)
                for comb in nex:
                    combs.append(comb + [i])
            
            return combs
        
        return search(0, 0)
    
