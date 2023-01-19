# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = accumulate(arr, initial=0)
        parity = [0, 0]
        subarrays = 0
        
        for num in prefix:
            subarrays += parity[1 - (num % 2)]
            parity[num % 2] += 1
            
        mod = pow(10, 9) + 7
        return subarrays % mod
    
