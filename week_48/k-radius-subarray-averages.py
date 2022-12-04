# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums) / 2:
            return [-1 for _ in nums]
        
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        result = [-1] * k
        for i in range(k, len(nums) - k):
            average = (prefix[i + k + 1] - prefix[i - k]) // ((2 * k) + 1)
            result.append(average)
        result += [-1] * k
        
        return result
    
