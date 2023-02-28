# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        nice = 0
        counter = Counter()
        counter[0] = 1
        
        for num in nums:
            prefix += num % 2
            nice += counter[prefix - k]
            counter[prefix] += 1
            
        return nice
    
