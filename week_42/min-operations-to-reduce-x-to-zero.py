# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def search(self, prefix, target, end):
        start = 0
        while start <= end:
            mid = (start + end) // 2
            if prefix[mid] > target:
                end = mid - 1
            elif prefix[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return -1
    
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [0]
        current = 0
        for i in range(len(nums)):
            prefix.append(nums[i] + current)
            current = prefix[-1]
            
        suffix = []
        current = 0
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(nums[i] + current)
            current = suffix[-1]
        suffix.reverse()
        suffix.append(0)
        
        best = inf
        for suf_idx, suf in enumerate(reversed(suffix)):
            pre_idx = self.search(prefix, x - suf, len(suffix) - suf_idx - 1)
            if pre_idx != -1:
                best = min(best, suf_idx + pre_idx)
                
        return best if best != inf else -1
    
