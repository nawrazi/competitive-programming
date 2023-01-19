# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = accumulate(nums, initial=0)
        mods = Counter()
        sums = 0
        
        for num in prefix:
            sums += mods[(k + num) % k]
            mods[num % k] += 1
            
        return sums
    
