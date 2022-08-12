# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len([c for c in Counter(nums).values() if c > 1])
        
        pool = set(nums)
        used = set()
        pairs = 0
        for num in nums:
            if num + k in pool and num + k not in used:
                pairs += 1
                used.add(num + k)
                
        for num in nums:
            if num - k in pool and num not in used:
                pairs += 1
                
        return pairs
    
