# https://leetcode.com/problems/distribute-repeating-integers/

class Solution:
    def backtrack(self, query, quantity, counts):
        if query >= len(quantity):
            return True
        
        for i, count in enumerate(counts):
            if count >= quantity[query]:
                counts[i] -= quantity[query]
                if self.backtrack(query + 1, quantity, counts):
                    return True
                counts[i] += quantity[query]
    
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        quantity.sort(reverse = True)
        counts = sorted(list(Counter(nums).values()), reverse = True)
        
        return self.backtrack(0, quantity, counts)
    
