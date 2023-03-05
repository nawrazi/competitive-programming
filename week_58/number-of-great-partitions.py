# https://leetcode.com/problems/number-of-great-partitions/description/

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        prefix = list(accumulate(nums))
        mod = pow(10, 9) + 7
        
        @cache
        def partition(idx, groupA):
            if idx >= len(nums):
                return k <= groupA <= prefix[-1] - k
            
            if groupA >= k and prefix[idx - 1] - groupA >= k:
                return pow(2, len(nums) - idx, mod)
            
            intoA = partition(idx + 1, groupA + nums[idx])
            intoB = partition(idx + 1, groupA)
            
            return (intoA + intoB) % mod
        
        return partition(0, 0)
    
