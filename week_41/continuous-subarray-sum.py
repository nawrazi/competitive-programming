# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
            prefix[-1] %= k
            
        first = {}
        for i, pre in enumerate(prefix):
            if pre not in first:
                first[pre] = i
            elif i - first[pre] > 1:
                return True
            
        return False
    
